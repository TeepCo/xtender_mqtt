#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
DEBUG = False
if DEBUG:
    import pydevd_pycharm
    pydevd_pycharm.settrace('localhost', port=10000, stdoutToServer=True, stderrToServer=True)

import paho.mqtt.client
import time
import sys
import os
import paho.mqtt.client as mqtt
import threading
import json
from contextlib import nullcontext

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '../scom/src')))

from sino import scom
from xtender_cfg import XtenderConfig

MQTT_ERROR_MSG = {
    0 :" Connection Accepted.",
    1 :" Connection Refused. Protocol level not supported.",
    2 :" Connection Refused. The client-identifier is not allowed by the server.",
    3 :" Connection Refused. The MQTT service is not available.",
    4 :" Connection Refused. The data in the username or password is malformed. Also check if you connecting to the right port.",
    5 :" Connection Refused. The client is not authorized to connect."
}

class XtenderMqttSender:
    """ Class for reading values from xtender devices and sending them to mqtt.

    This class finds Xtender devices connected to the network, reads data from them and sends the data to the mqtt message broker afterwards.
    It is necessary to configure both the communication with Xtenders and the mqtt message broker.
    You can do so by providing correct values in the `xtender_config/user_config.yaml` configuration file.
    Values read from Xtender can have two priority levels, urgent or normal. There is a dedicated thread for values with either priority.
    Values with normal priority wait for `loop_sleep` seconds (default 5, can be changed). Values with urgent priority do not wait.

    Attributes:
        device_not_disconnected (bool): Used for detecting unexpected device disconnection. When False, both threads will exit.
        lock (threading.Lock)
        config (XtenderConfig): Default and user modified configuration values.
        logger (Logger)
        client (paho.mqtt.Client): Mqtt message broker
        device_manager (scom.dman.DeviceManager): Scom device manager
        device_observer: Scom device observer
    """

    def __init__(self, xtender_config: XtenderConfig):
        self.device_not_disconnected: bool = True
        self.lock: threading.Lock = threading.Lock()
        self.config: XtenderConfig = xtender_config
        self.logger = xtender_config.logger
        self.logger.info("Configuration loaded")

        self.client: mqtt.Client = connect_mqtt(self.config, self.logger)
        self.subscribe_mqtt("xtender/+/parameters/+/set")
        self.client.loop_start()

        self.device_manager: scom.dman.DeviceManager = self.configure_and_connect_device_manager()
        self.logger.info(f"found {len(self.device_manager._device)} devices.")
        self.device_observer = ScomDevicesObserver(self)

    def proc_main_send_loop(self, urgent=False) -> None:
        """ Main loop that reads parameters from Xtenders and pushes them to the dequeue

        Attempts to read data from all Xtender devices - specifically parameters and user
        info - and sends them to the mqtt message broker. The actual reading and value sending is done in two methods:
        `read_and_publish_param` and `read_and_publish_user_info`. Normal loop waits for `config.loop_sleep_seconds`
        after values are read and sent, urgent loop does not wait.

        Args:
            urgent (bool): Boolean that specifies whether the loop is urgent or not.
        """

        if urgent:
            self.logger.info("Urgent sensor loop started")
        else:
            self.logger.info("Normal sensor loop started")
        while self.device_not_disconnected:

            time.sleep(1)

            for device_address in self.device_manager._device.copy():
                self.logger.debug(f"Reading values from device address {device_address} urgent:{urgent}")
                try:
                    device = self.device_manager._device[device_address]
                except KeyError:
                    self.logger.error(f"Device {device_address} not found")
                    self.device_not_disconnected = False
                    break

                user_info_table_extended = get_extended_user_info_table(device)
                param_counter = 0
                for param_value in user_info_table_extended.items():
                    param_number = param_value[1]['number']
                    if (urgent and param_number in self.config.urgent_list) or (not urgent and param_number not in self.config.urgent_list):
                        self.read_and_publish_user_info(param_value, device)
                        param_counter += 1

                param_info_table_extended = get_extended_param_info_table(device)
                param_counter = 0
                for param_value in param_info_table_extended.items():
                    param_number = param_value[1]['number']
                    if (urgent and param_number in self.config.urgent_list) or  (not urgent and param_number not in self.config.urgent_list):
                        self.read_and_publish_param(param_value, device)
                        param_counter += 1

            if not urgent:
                self.logger.debug(f"Waiting {self.config.loop_sleep}s")
                time.sleep(self.config.loop_sleep)
            else:
                self.logger.debug("Not waiting due to urgent ")


    def configure_and_connect_device_manager(self) -> scom.dman.DeviceManager:
        """Configures and connects to the scom device manager based on values provided in the configuration files.

        Returns:
            Scom device manager
        """

        # Create device manager detecting devices on the SCOM bus
        device_manager = scom.dman.DeviceManager(config=self.config.device_manager_config,
                                                 control_interval_in_seconds=5.0)
        return device_manager

    def read_and_publish_param(self, param_value, device, lock=True) -> None:
        """ Reads parameter value from xtender and sends them via mqtt.

        If the parameter is enabled in the configuration file the value is read from Xtender device and
        sent via mqtt. If the reading fails, all the threads are killed instantly and the program immediately exits.
        Args:
            param_value (tuple(int,int)): Parameter value.
            device (scom.Device.SD_XTENDER): Xtender device.
            lock (bool): Boolean to indicate whether to acquire the threading lock.
        """
        device_address = device.device_address
        param_name = param_value[1]['name']
        param_number = int(param_value[1]['number'])
        if not self.config.parameters_config[param_name]['enabled']:
            self.logger.debug(f"Parameter {param_number} {param_name} is disabled")
            return

        with self.lock if lock else nullcontext():
            if format == 'signal':
                value = 'SIGNAL'
            self.logger.debug(f"Read value: {param_name} {device_address}:{param_number}")
            try:
                value = device._read_parameter_info(param_name)

            except Exception as e:

                self.logger.error(e.args)
                self.logger.error(f"Value error: {param_name} {device_address}:{param_number}")
                os._exit(1)

            # sending value
            topic = f"{self.config.mqtt_root_prefix}/{device_address}/parameters/{param_name}"
            payload = value
            self.send_and_check_mqqtt_delivery(topic, payload)

            # sending value info
            value_info = json.dumps(param_value[1])
            payload = json.dumps(value_info)
            self.send_and_check_mqqtt_delivery(topic, payload)


    def send_and_check_mqqtt_delivery(self,topic,payload):
        message_info = self.client.publish(topic,payload)
        if 0 < message_info.rc <= 5:
            self.logger.error(MQTT_ERROR_MSG[message_info.rc])
            if message_info.rc != 3:
                sys.exit(1)
        elif message_info.rc > 5:
            self.logger.error(f"MQTT returned code {message_info.rc}. Check Documentation")



    def read_and_publish_user_info(self, param_value, device, lock=True) -> None:
        """ Reads sensors value from xtender and sends them via mqtt.

        If the sensor is enabled in the configuration file a value is read from Xtender device and
        sent via mqtt. If the reading fails, all the threads are killed instantly and the program immediately exits.

        Args:
            param_value (): Parameter value.
            device (scom.Device.SD_XTENDER): Xtender device.
            lock (bool): Boolean to indicate whether to acquire the threading lock.
        """
        device_address = device.device_address
        param_name = param_value[1]['name']
        param_number = int(param_value[1]['number'])
        if not self.config.sensors_config[param_name]['enabled']:
            self.logger.debug(f"Parameter {param_number} {param_name} is disabled")
            return

        property_format = param_value[1]['propertyFormat']

        with self.lock if lock else nullcontext():

            self.logger.debug(f"Read value: {param_name} {device_address}:{param_number}")
            try:
                data_value = device.get_value(param_number, property_format)
            except Exception as e:
                self.logger.error(e.args)
                self.logger.error(f"Value error: {param_name} {device_address}:{param_number}")
                os._exit(1)

            self.logger.debug(f"Got value: {param_name} {device_address}:{param_number} = {data_value}")
            if property_format == 'float':
                value = str(data_value)
            elif property_format == 'enum':
                hass_cfg = self.config.mqtt_discovery_map.get(param_name, None)
                if hass_cfg:
                    enum_map = hass_cfg.get('enum_map')
                    if enum_map:
                        value = enum_map[data_value]
                    else:
                        self.logger.error("Could not load enum map from hass_cfg")

            # sending value
            topic = f"{self.config.mqtt_root_prefix}/{device_address}/values/{param_name}"
            payload = value
            self.send_and_check_mqqtt_delivery(topic, payload)

            topic = f"{self.config.mqtt_root_prefix}/{device_address}/parameters/{param_name}/"
            value_info = json.dumps(param_value[1])
            payload = json.dumps(value_info)
            self.send_and_check_mqqtt_delivery(topic,payload)

    def subscribe_mqtt(self, topic) -> None:
        """ Subscribes to the mqtt message broker.

        Args:
            topic (str): Mqtt topic
        """
        def on_message(client, userdata, msg):
            self.logger.info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            # xtender/101/parameters/allowInverter/set'
            topic = msg.topic.split('/')
            msg_payload = msg.payload.decode()

            device_address = int(topic[1])
            parameter_id = topic[3]

            print(f"{device_address} {parameter_id} {msg_payload}")
            device = self.device_manager._device[int(topic[1])]
            param_value = (parameter_id, get_extended_param_info_table(device)[parameter_id])
            param_number = get_extended_param_info_table(device)[parameter_id]['number']
            param_format = get_extended_param_info_table(device)[parameter_id]['propertyFormat']
            # device.set_value(param_number, param_format, payload)
            # 'float', 'int32', 'enum', 'byte', 'bool'
            if param_format == 'float':
                payload = round(float(msg_payload), 1)
            elif param_format == 'int32':
                payload = int(msg_payload)
            elif param_format == 'bool':
                payload = int(msg_payload)
            elif param_format == 'byte':
                payload = bytes(msg_payload)
            else:
                self.logger.error(f"Could not write parameter: Unsupported parameter format {param_format}")
                return

            with self.lock:
                try:
                    device._write_parameter(int(param_number), payload, param_format)
                    success = True
                    self.logger.ingo(f"Write successful:  {param_number} = {payload}")
                except:
                    self.logger.error(f"Could not write parameter {param_number} => {payload}")
                finally:
                    if success:
                        result = "Ok"
                    else:
                        result = "Error"
                    client.publish(f"xtender/{device_address}/dbg/last_cmd_result", result)

            self.logger.info("Loadig state again...")
            self.read_and_publish_param(param_value, device, False)

        result, _ = self.client.subscribe(topic)
        if result == paho.mqtt.client.MQTT_ERR_SUCCESS:
            self.logger.info(f"Successfully subscribed to MQTT topic {topic}")
        elif paho.mqtt.client.MQTT_ERR_NO_CONN:
            self.logger.error(f"Client is not connected to MQTT, errror subscribing to topic {topic}. Check your mqtt settings.")

        self.client.on_message = on_message

def send_device_discovery(client, device_manager, address, config, logger) -> None:
    """Home assistant mqtt discovery.

    Args:
        client (mqtt.Client): Mqtt client
        device_manager (scom.dman.DeviceManager): Scom device manager.
        address (int): The device number on the SCOM interface. Own address of the device.
        config (XtenderConfig): Default and user changed configurations.
        logger (logging.logger): Logger.
    """
    logger.info(f"Sending hassio discovery for device {address}")
    device = device_manager._device[address]
    device_address = device.device_address


    for param_key in config.mqtt_discovery_map:
        rule = config.mqtt_discovery_map[param_key]
        deconfig = False
        if rule['param']:
            if not config.parameters_config[param_key]['enabled']:
                logger.debug(f"Discovery rule for {param_key} is disabled")
                # continue
                deconfig = True
        else:
            if not config.sensors_config[param_key]['enabled']:
                logger.debug(f"Discovery rule for {param_key} is disabled")
                # continue
                deconfig = True

        component = rule['component']
        icon = rule.get('icon', None)
        unit_of_measurement = rule.get('unit_of_measurement', None)

        if rule['param']:
            payload_topic = f"xtender/{device_address}/parameters/{param_key}"
            # name = device.paramInfoTable[param_key]['studerName']
            name = get_extended_param_info_table(device)[param_key]['studerName']
        else:
            payload_topic = f"xtender/{device_address}/values/{param_key}"
            # name = device.userInfoTable[param_key]['studerName']
            name = get_extended_user_info_table(device)[param_key]['studerName']

        device_type_str = [k for k, v in device.device_categories.items() if v == device.device_type]

        unique_id = f"{rule['number']}_{device_address}_{param_key}"

        discovery_topic = f"{config.discovery_base_topic}/{component}/{unique_id}/{param_key}/config"

        logger.debug("Discovery topic=" + discovery_topic)

        discovery_json = {
            "unique_id": unique_id,
            "object_id": unique_id,
            "name": name,
            "state_topic": payload_topic,
            "device": {
                "name": f"Xtender ({device_address})",
                "identifiers": f"Xtender ({device_address})",
            }
        }
        if rule.get('device_class', None):
            discovery_json.update({
                "device_class": rule['device_class'],
            })
        if unit_of_measurement:
            discovery_json.update({
                "unit_of_measurement": rule['unit_of_measurement']
            })
        if icon:
            discovery_json.update({
                "icon": icon
            })
        if rule['param']:
            discovery_json.update({
                "command_topic": f"{payload_topic}/set",
                "entity_category": "config",
            })
        if component == 'switch':
            if rule.get('payload_on', None):
                discovery_json.update({
                    "payload_on": rule['payload_on'],
                    "payload_off": rule['payload_off']
                })
            else:
                discovery_json.update({
                    "payload_on": 1,
                    "payload_off": 0
                })
        elif component == 'button':
            discovery_json.update({
                "payload_press": 1,
            })
        elif component == 'number':
            discovery_json.update({
                "min": rule['min'],
                "max": rule['max'],
                "step": rule['step'],
                "mode": 'box'
            })

        if deconfig:
            discovery_payload = ""
            logger.info(f"Unregistering {unique_id} / {param_key}")
        else:
            discovery_payload = json.dumps(discovery_json)

        client.publish(discovery_topic, discovery_payload, retain=True)

def get_extended_param_info_table(device):
    return device.paramInfoTable


def get_extended_user_info_table(device):
    return device.userInfoTable


class ScomDevicesObserver(scom.dman.DeviceSubscriber):
    """Receives device notifications if DeviceManager finds Studer devices.
    """

    def __init__(self, xtender: XtenderMqttSender):
        super(ScomDevicesObserver, self).__init__()
        self.xtender = xtender
        xtender.device_manager.subscribe(self)

    def on_device_connected(self, device):

        if device.device_type == scom.Device.SD_XTENDER:
            print('Xtender found!')
            send_device_discovery(self.xtender.client, self.xtender.device_manager, device.device_address, self.xtender.config, self.xtender.logger)
        else:
            print('Other device type detected')

    def on_device_disconnected(self, device):
        print(f"DEVICE DISCONNECTED")
        self.xtender.logger.error(f"Device {device.device_address} disconnected !")
        self.xtender.device_not_disconnected = False
        # print(f"!!!!{device} disconnected")




def connect_mqtt(xtender_config : XtenderConfig,logger) -> mqtt.Client:
    """ Sets up mqtt client and attempts to connect to the message broker.

    Args:
        xtender_config (XtenderConfig): Default and user changed configurations.
        logger (logging.logger): Logger.
    Returns:
        Mqtt client
    """
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            # print("Connected to MQTT MQTT_BROKER!")
            logger.info("MQTT connection is active")

        else:
            logger.error(MQTT_ERROR_MSG[rc]) if rc <= 5 else logger.error(f"MQTT returned code {rc}")

    # Set Connecting Client ID
    logger.info("Connecting to mqtt...")
    client = mqtt.Client(xtender_config.mqtt_client_id)
    client.username_pw_set(xtender_config.mqtt_username, xtender_config.mqtt_password)
    client.on_connect = on_connect

    try:
        client.connect(xtender_config.mqtt_broker, xtender_config.mqtt_port)

    except OSError as e:
        if e.errno == 113:
            logger.error(f"Could not connect to {xtender_config.mqtt_broker}: No route to host")
            sys.exit(1)
    return client



def main():
    """ Starts threads.

    Creates XtenderConfig and XtenderMqttSender classes and starts producer
    (urgent and normal value reading and pushing them to deque) and consumer
    (sending from deque via mqtt) threads.

    """
    xtender_config = XtenderConfig(debug=False)
    xtender = XtenderMqttSender(xtender_config=xtender_config)

    time.sleep(5)
    # send_discovery(client, device_manager)
    send_loop_urgent = threading.Thread(target=xtender.proc_main_send_loop, args=(True,))
    send_loop_normal = threading.Thread(target=xtender.proc_main_send_loop, args=(False,))
    # send_to_mqtt = threading.Thread(target=xtender.send_to_mqtt_from_queue)
    send_loop_urgent.start()
    send_loop_normal.start()

    if not send_loop_normal.is_alive() and send_loop_urgent.is_alive():
        xtender.logger.error("Threads were not started!")

    # send_to_mqtt.start()
    #while xtender.all_ok:
    #    pass

if __name__ == '__main__':
    # logger.info("Starting..")
    main()
