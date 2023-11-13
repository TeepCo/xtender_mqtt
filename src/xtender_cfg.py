# pro pycharm debug, True = ceka na pycharm
import json
import yaml
from enum import Enum
from default_xtender_values import DefaultValues
import logging
import logging.config
import os


class FileType(Enum):
    JSON = 0
    YAML = 1

class XtenderConfig(DefaultValues):
    def __init__(self, debug=False):
        self.debug = False
        self.xtender_config_folder_name = "config"
        self.path_to_config_dir = os.path.join(os.getcwd(), f"../{self.xtender_config_folder_name}/")
        self.user_config_file_name = "user_config.yaml"
        self._user_config: dict = self.load_config_file(self.path_to_config_dir + self.user_config_file_name, FileType.YAML)

        # These settings have to be filled. Program cannot run without them
        try:
            self._user_mqtt_config: dict = self._user_config['mqtt_setup']
            self.logging_config: dict = self._user_config['logging']
            self._device_manager_config: dict = self._user_config['device_manager_config']

        except KeyError as e:
            raise Exception(f"Parameter {e.args[0]} was not set in {self.path_to_config_dir}/{self.user_config_file_name}") from e

        # These settings are optional - if not found, default values are used instead.

        try:
            self.discovery_base_topic: dict = self._user_config['discovery_base_topic']
            self._user_sensors_config: dict = self._user_config['sensors']
            self._user_parameters_config: dict = self._user_config['parameters']
            self.urgent_list: list = self._user_config['urgent_list']
            self.loop_sleep = self._user_config['loop_sleep']
        except KeyError:
            pass

        self._update_user_preferences()

    def _setup_logging(self):
        try:
            logging.config.dictConfig(self.logging_config)
        except KeyError as e:
            raise Exception("") #TODO finish
        self.logger = logging.getLogger('xtender_mqtt')
        self.scom_logger = logging.getLogger('scom_logger')





    def _update_user_preferences(self) -> None:
        """
        Overwrites default settings with user preferences specified in [path_to_config_dir]/user_config.yaml
        """
        self._setup_logging()

        try:
            self.mqtt_username = self._user_mqtt_config['mqtt_username']
            self.mqtt_broker = self._user_mqtt_config['mqtt_broker']
            self.mqtt_password = self._user_mqtt_config['mqtt_password']
            self.mqtt_port = self._user_mqtt_config['mqtt_port']
            self.mqtt_client_id = self._user_mqtt_config['mqtt_client_id']
            self.mqtt_root_prefix: dict = self._user_mqtt_config['mqtt_root_prefix']
        except KeyError as e:
            raise Exception(f"Error reading values in mqtt_setup section in {self.path_to_config_dir}/{self.user_config_file_name}") from e

        if hasattr(self, '_user_parameters_config'):
            for parameter_name, value in self._user_parameters_config.items():
                self.parameters_config[parameter_name]['enabled'] = value
        if hasattr(self, '_user_sensors_config'):
            for sensor_name, value in self._user_sensors_config.items():
                self.sensors_config[sensor_name]['enabled'] = value

        try:
            self.device_manager_config['scom'] = self._device_manager_config['scom']
            self.device_manager_config['scom-device-address-scan']['xtender'] =[101,100+self._device_manager_config['number_of_scom_devices']['xtender']]
        except KeyError as e:
            raise Exception(f"Error reading values in device_manager_config section in {self.path_to_config_dir}/{self.user_config_file_name}") from e


    def load_config_file(self, path_to_file:str, file_type:FileType):
        try:
            with open(path_to_file) as f:
                if file_type == FileType.JSON:
                    config = json.load(f)
                elif file_type == FileType.YAML:
                    config = yaml.load(f, yaml.SafeLoader)
        except FileNotFoundError as e:
            raise Exception(f"Error reading file {path_to_file}, from folder {self.path_to_config_dir}") from e
        except json.decoder.JSONDecodeError as e:
            raise Exception("Conversion from json failed. Please check your json config files.") from e
        except yaml.YAMLError as e:
            raise Exception("Conversion from yaml failed. Please check your yaml config files.") from e
        if not isinstance(config, dict):
            raise Exception(f"Error loading config file {path_to_file}, expected type is {dict}, got {type(config)}")
        return config

