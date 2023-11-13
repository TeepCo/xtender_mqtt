class DefaultValues:
    urgent_list = [3022]
    mqtt_root_prefix = 'xtender'
    discovery_base_topic = "homeassistant"
    mqtt_client_id = 'xtender-mqtt-001'
    mqtt_username = 'homeassistant'
    mqtt_broker = '10.10.10.10'
    mqtt_password = 'ohv6reivi8ievaisooLoiFo6ChuPei2ue3ahjoh4yooyah3einooheza6wei6gie'
    mqtt_port = 1883
    loop_sleep = 5  # time to wait after loading data from all devices

    device_manager_config = {
        'scom': {
            'interface': '/dev/ttyUSB0',
            'baudrate': '38400'
        },
        'scom-device-address-scan': {
            'xtender': [101, 106]
        }
    }

    # SENSORS
    sensors_config = {
        "batteryVoltage": {
            "name": "batteryVoltage",
            "number": 3000,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Battery voltage",
            "enabled": True
        },
        "batteryChargeReferenceCurrent": {
            "name": "batteryChargeReferenceCurrent",
            "number": 3004,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Wanted battery charge current",
            "enabled": True
        },
        "batteryCurrent": {
            "name": "batteryCurrent",
            "number": 3005,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Battery charge current",
            "enabled": True
        },
        "soc": {
            "name": "soc",
            "number": 3007,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "State of charge",
            "enabled": False
        },
        "batteryCyclePhase": {
            "name": "batteryCyclePhase",
            "number": 3010,
            "propertyFormat": "enum",
            "default": 0,
            "studerName": "Battery cycle phase",
            "enabled": False
        },
        "pvVoltage": {
            "name": "pvVoltage",
            "number": 3011,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Input voltage",
            "enabled": False
        },
        "inputVoltage": {
            "name": "inputVoltage",
            "number": 3011,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Input voltage",
            "enabled": True
        },
        "inputCurrent": {
            "name": "inputCurrent",
            "number": 3012,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Input current",
            "enabled": True
        },
        "busVoltage": {
            "name": "busVoltage",
            "number": 3021,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Output voltage",
            "enabled": False
        },
        "outputVoltage": {
            "name": "outputVoltage",
            "number": 3021,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Output voltage",
            "enabled": True
        },
        "outputCurrent": {
            "name": "outputCurrent",
            "number": 3022,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Output current",
            "enabled": True
        },
       "operatingMode": {
           "name": "operatingMode",
            "number": 3028,
            "propertyFormat": "enum",
            "default": 0,
            "studerName": "Operating mode",
            "enabled": True
        },
        "inputFrequency": {
            "name": "inputFrequency",
            "number": 3084,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Input frequency",
            "enabled": False
        },
        "inverterEnabled": {
            "name": "inverterEnabled",
            "number": 3049,
            "propertyFormat": "enum",
            "default": 0,
            "studerName": "State of the inverter",
            "enabled": True
        },
        "lockingsFlag": {
            "name": "lockingsFlag",
            "number": 3056,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "LockingsFlag",
            "enabled": True
        },
        "softVersionMsb": {
            "name": "softVersionMsb",
            "number": 3130,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "ID SOFT msb",
            "enabled": False
        },
        "softVersionLsb": {
            "name": "softVersionLsb",
            "number": 3131,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "ID SOFT lsb",
            "enabled": False
        },
        "acInjectionCurrentLimitation": {
            "name": "acInjectionCurrentLimitation",
            "number": 3158,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "AC injection current limited (ARN4105)",
            "enabled": False
        },
        "acInjectionCurrentLimitationReason": {
            "name": "acInjectionCurrentLimitationReason",
            "number": 3159,
            "propertyFormat": "enum",
            "default": 0,
            "studerName": "AC injection current, type of limitation (ARN4105)",
            "enabled": False
        },
        "sourceOfLimitation": {
            "name": "sourceOfLimitation",
            "number": 3160,
            "propertyFormat": "enum",
            "default": 0,
            "studerName": "Source of limitation in charger and injector mode",
            "enabled": False
        },
        "batteryPriorityActive": {
            "name": "batteryPriorityActive",
            "number": 3161,
            "propertyFormat": "enum",
            "default": 0,
            "studerName": "Battery priority active",
            "enabled": False
        },
        "forcedGridFeedingActive": {
            "name": "forcedGridFeedingActive",
            "number": 3162,
            "propertyFormat": "enum",
            "default": 0,
            "studerName": "Forced grid feeding active",
            "enabled": False
        },

        "operatingState": {
            "name": "remoteEntryActivate",
            "number": 3028,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Operating state",
            "enabled": False
        },


        "outputActivePowerMin": {
            "number": 3101,
            "param": False,
            "component": "sensor",
            "device_class": "power",
            "icon": None,
            "unit_of_measurement": "kW",
            "enabled": True
        },
        "inputActivePowerMin": {
            "number": 3119,
            "param": False,
            "component": "sensor",
            "device_class": "power",
            "icon": None,
            "unit_of_measurement": "kW",
            "enabled": True
        },
        "stateOfTransferRelay": {
            "number": 3020,
            "enabled": True
        },
        "energyACInCurrentDay": {
            "number": 3080,
            "enabled": True
        },
        "battDischargeCurrentDay": {
            "number": 3074,
            "enabled": True
        },
        "consumersEnergyCurrentDay": {
            "number": 3083,
            "enabled": True
        }

    }



    # PARAMETRS
    parameters_config = {
        "powerOnXtender": {
            "number": 1576,
            "propertyFormat": "bool",
            "default": False,
            "studerName": "ON/OFF command",
            "enabled": False
        },
        "powerOnAllXtenders": {
            "name": "powerOnAllXtenders",
            "number": 1415,
            "propertyFormat": "signal",
            "default": False,
            "studerName": "ON of the Xtenders",
            "enabled": False
        },
        "powerOffAllXtenders": {
            "name": "powerOffAllXtenders",
            "number": 1399,
            "propertyFormat": "signal",
            "default": False,
            "studerName": "ON of the Xtenders",
            "enabled": False
        },
        "resetAllInverters": {
            "name": "resetAllInverters",
            "number": 1468,
            "propertyFormat": "signal",
            "default": False,
            "studerName": "Reset all of the inverters",
            "enabled": False
        },
        "maximumAcInputCurrent": {
            "name": "maximumAcInputCurrent",
            "number": 1107,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Maximum current of AC source (input limit)",
            "enabled": False
        },
        "allowInverter": {
            "name": "allowInverter",
            "number": 1124,
            "propertyFormat": "bool",
            "default": True,
            "studerName": "Inverter allowed",
            "enabled": True
        },
        "allowCharger": {
            "name": "allowCharger",
            "number": 1125,
            "propertyFormat": "bool",
            "default": True,
            "studerName": "Charger allowed",
            "enabled": True
        },
        "batteryChargeReferenceCurrent": {
            "name": "batteryChargeReferenceCurrent",
            "number": 1138,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Battery charge current",
            "enabled": True
        },
        "standbyPowerLevel": {
            "name": "standbyPowerLevel",
            "number": 1187,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Standby level",
            "enabled": False
        },
        "restoreDefaultSettings": {
            "name": "restoreDefaultSettings",
            "number": 1395,
            "propertyFormat": "signal",
            "default": False,
            "studerName": "Restore Default Settings",
            "enabled": False
        },
        "restoreFactorySettings": {
            "name": "restoreFactorySettings",
            "number": 1287,
            "propertyFormat": "signal",
            "default": False,
            "studerName": "Restore Factory Settings",
            "enabled": False
        },
        "batteryMinimumVoltageWithoutLoad": {
            "name": "batteryMinimumVoltageWithoutLoad",
            "number": 1108,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Battery undervoltage level without load",
            "enabled": True
        },
        "batteryMinimumVoltageWithLoad": {
            "name": "batteryMinimumVoltageWithLoad",
            "number": 1109,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Battery undervoltage level without load",
            "enabled": True
        },
        "batteryMaximumVoltage": {
            "name": "batteryMaximumVoltage",
            "number": 1121,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Battery overvoltage level",
            "enabled": True
        },
        "floatingVoltage": {
            "name": "floatingVoltage",
            "number": 1140,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Floating voltage",
            "enabled": True
        },
        "forceFloatingPhase": {
            "name": "forceFloatingPhase",
            "number": 1467,
            "propertyFormat": "signal",
            "default": False,
            "studerName": "Force phase of floating",
            "enabled": False
        },
        "forceNewChargeCycle": {
            "name": "forceNewChargeCycle",
            "number": 1142,
            "propertyFormat": "signal",
            "default": False,
            "studerName": "Force a new cycle",
            "enabled": False
        },
        "autoAcInputCurrentReduction": {
            "name": "autoAcInputCurrentReduction",
            "number": 1527,
            "propertyFormat": "bool",
            "default": False,
            "studerName": "Decrease max input limit current with AC-In voltage",
            "enabled": False
        },
        "boostPhaseAllowed": {
            "name": "boostPhaseAllowed",
            "number": 1155,
            "propertyFormat": "bool",
            "default": True,
            "studerName": "Absorption phase allowed",
            "enabled": False
        },
        "boostVoltage": {
            "name": "boostVoltage",
            "number": 1156,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Absorption voltage",
            "enabled": False
        },
        "inputCurrentAdaptionRange": {
            "name": "inputCurrentAdaptionRange",
            "number": 1433,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Adaptation range of the input current according to the input voltage",
            "enabled": False
        },
        "gridFeedingAllowed": {
            "name": "gridFeedingAllowed",
            "number": 1127,
            "propertyFormat": "bool",
            "default": False,
            "studerName": "Grid feeding allowed",
            "enabled": False
        },
        "gridFeedingMaximumCurrent": {
            "name": "gridFeedingMaximumCurrent",
            "number": 1523,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Max grid feeding current",
            "enabled": False
        },
        "gridFeedingBatteryVoltage": {
            "name": "gridFeedingBatteryVoltage",
            "number": 1524,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Battery voltage target for forced grid feeding",
            "enabled": False
        },
        "gridFeedingStartTime": {
            "name": "gridFeedingStartTime",
            "number": 1525,
            "propertyFormat": "int32",
            "default": 0,
            "studerName": "Forced grid feeding start time",
            "enabled": False
        },
        "gridFeedingStopTime": {
            "name": "gridFeedingStopTime",
            "number": 1526,
            "propertyFormat": "int32",
            "default": 0,
            "studerName": "Forced grid feeding stop time",
            "enabled": False
        },
        "frequencyControlEnabled": {
            "name": "frequencyControlEnabled",
            "number": 1627,
            "propertyFormat": "bool",
            "default": False,
            "studerName": "ARN4105 frequency control enabled",
            "enabled": False
        },
        "batteryPriorityAsEnergySource": {
            "name": "batteryPriorityAsEnergySource",
            "number": 1296,
            "propertyFormat": "bool",
            "default": False,
            "studerName": "Batteries priority as energy source",
            "enabled": False
        },
        "batteryPriorityVoltage": {
            "name": "batteryPriorityVoltage",
            "number": 1297,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Battery priority voltage",
            "enabled": False
        },
        "batteryVoltageToDeactivate": {
            "name": "batteryVoltageToDeactivate",
            "number": 1255,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Battery voltage to deactivate (AUX 1)",
            "enabled": True
        },
        "remoteEntryActivate": {
            "name": "remoteEntryActivate",
            "number": 1545,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Remote entry active",
            "enabled": True
        },
        "chargerAllowed": {
            "name": "chargerAllowed",
            "number": 1125,
            "propertyFormat": "float",
            "default": 0.0,
            "studerName": "Charger allowed",
            "enabled": False
        }
}
    # MQTT discovery map
    mqtt_discovery_map = {
        'batteryVoltage': {
            'number': 3000,
            'param': False,
            'component': 'sensor',
            'device_class': 'voltage',
            'icon': None,
            'unit_of_measurement': 'V',
        },
        'batteryChargeReferenceCurrent': {
            'number': 3004,
            'param': False,
            'component': 'sensor',
            'device_class': 'current',
            'icon': None,
            'unit_of_measurement': 'A',
        },
        'batteryCurrent': {
            'number': 3005,
            'param': False,
            'component': 'sensor',
            'device_class': 'current',
            'icon': None,
            'unit_of_measurement': 'A',
        },
        'soc': {
            'number': 3007,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'unit_of_measurement': '%',
        },
        'batteryCyclePhase': {
            'number': 3010,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'enum_map': {
                0: 'Invalid value',
                1: 'Bulk',
                2: 'Absorpt.',
                3: 'Equalise',
                4: 'Floating',
                5: 'R.float.',
                6: 'Per.abs.',
                7: 'Mixing',
                8: 'Forming'
            }
        },
        'pvVoltage': {
            'number': 3011,
            'param': False,
            'component': 'sensor',
            'device_class': 'voltage',
            'icon': None,
            'unit_of_measurement': 'V',
        },
        'inputVoltage': {
            'number': 3011,
            'param': False,
            'component': 'sensor',
            'device_class': 'voltage',
            'icon': None,
            'unit_of_measurement': 'V',
        },
        'inputCurrent': {
            'number': 3012,
            'param': False,
            'component': 'sensor',
            'device_class': 'current',
            'icon': None,
            'unit_of_measurement': 'A',
        },
        # 'busVoltage': {
        #     'number': 3021,
        #     'param': False,
        #     'component': 'sensor',
        #     'device_class': 'voltage',
        #     'icon': None,
        #     'unit_of_measurement': 'V',
        # },
        'outputVoltage': {
            'number': 3021,
            'param': False,
            'component': 'sensor',
            'device_class': 'voltage',
            'icon': None,
            'unit_of_measurement': 'V',
        },
        'outputCurrent': {
            'number': 3022,
            'param': False,
            'component': 'sensor',
            'device_class': 'current',
            'icon': None,
            'unit_of_measurement': 'A',
        },
        'operatingMode': {
            'number': 3028,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'unit_of_measurement': None,
            'enum_map': {
                0: 'Invalid value',
                1: 'Inverter',
                2: 'Charger',
                3: 'Boost',
                4: 'Injection'
            }
        },
        'inputFrequency': {
            'number': 3084,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'unit_of_measurement': None,
        },
        'inverterEnabled': {
            'number': 3049,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'enum_map': {
                0: 'Off',
                1: 'On'
            }
        },
        'lockingsFlag': {
            'number': 3056,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'unit_of_measurement': None,
        },
        'softVersionMsb': {
            'number': 3130,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'unit_of_measurement': None,
        },
        'softVersionLsb': {
            'number': 3131,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'unit_of_measurement': None,
        },
        'acInjectionCurrentLimitation': {
            'number': 3158,
            'param': False,
            'component': 'sensor',
            'device_class': 'current',
            'icon': None,
            'unit_of_measurement': 'A',
        },
        'acInjectionCurrentLimitationReason': {
            'number': 3159,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'enum_map': {
                0: 'No limit',
                1: 'FreezeOF',
                2: 'N_ImaxOF',
                3: 'FreezeUF',
                4: 'N_ImaxUF',
                5: 'N_IMaxST'
            }
        },
        'sourceOfLimitation': {
            'number': 3160,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'unit_of_measurement': None,
            'enum_map': {
                0: 'Invalid value',
                1: 'Ubatt',
                2: 'Ubattp',
                3: 'Ubattpp',
                4: 'Ibatt',
                5: 'Pchar',
                6: 'UbattInj',
                7: 'Iinj',
                8: 'Imax',
                9: 'Ilim',
                10: 'Ithermal',
                11: 'PchNeg',
                12: 'ARN f',
            }
        },
        'batteryPriorityActive': {
            'number': 3161,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'unit_of_measurement': None,
            'enum_map': {
                0: 'Off',
                1: 'On'
            }
        },
        'forcedGridFeedingActive': {
            'number': 3162,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'enum_map': {
                0: 'Off',
                1: 'On'
            }
        },

        'outputActivePowerMin': {
            'number': 3101,
            'param': False,
            'component': 'sensor',
            'device_class': 'power',
            'icon': None,
            'unit_of_measurement': 'kW',
        },
        'inputActivePowerMin': {
            'number': 3119,
            'param': False,
            'component': 'sensor',
            'device_class': 'power',
            'icon': None,
            'unit_of_measurement': 'kW',
        },
        'stateOfTransferRelay': {
            'number': 3020,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'enum_map': {
                0: 'Opened',
                1: 'Closed'
            }
        },
        'energyACInCurrentDay': {
            'number': 3080,
            'param': False,
            'component': 'sensor',
            'device_class': 'energy',
            'icon': None,
            'unit_of_measurement': 'kWh',
        },
        'battDischargeCurrentDay': {
            'number': 3074,
            'param': False,
            'component': 'sensor',
            'device_class': 'energy',
            'icon': None,
            'unit_of_measurement': 'kWh',
        },
        'consumersEnergyCurrentDay': {
            'number': 3083,
            'param': False,
            'component': 'sensor',
            'device_class': 'energy',
            'icon': None,
            'unit_of_measurement': 'kWh',
        },

        'powerOnXtender': {
            'number': 1576,
            'param': True,
            'component': 'switch'
        },
        'powerOnAllXtenders': {
            'number': 1415,
            'param': True,
            'component': 'button'
        },
        'powerOffAllXtenders': {
            'number': 1399,
            'param': True,
            'component': 'button'
        },
        'resetAllInverters': {
            'number': 1468,
            'param': True,
            'component': 'button'
        },
        'maximumAcInputCurrent': {
            'number': 1107,
            'param': True,
            'component': 'number',
            'min': 2,
            'max': 50,
            'step': 1
        },
        'allowInverter': {
            'number': 1124,
            'param': True,
            'component': 'switch'
        },
        'allowCharger': {
            'number': 1125,
            'param': True,
            'component': 'switch'
        },

        # 'batteryChargeReferenceCurrent': {
        #     'number': 1138,
        #     'param': True,
        #     'component': 'number'
        # },
        'standbyPowerLevel': {
            'number': 1187,
            'param': True,
            'component': 'number',
            'min': 0,
            'max': 200,
            'step': 1
        },
        'restoreDefaultSettings': {
            'number': 1395,
            'param': True,
            'component': 'button'
        },
        'restoreFactorySettings': {
            'number': 1287,
            'param': True,
            'component': 'button'
        },
        'batteryMinimumVoltageWithoutLoad': {
            'number': 1108,
            'param': True,
            'component': 'number',
            'device_class': 'voltage',
            'unit_of_measurement': 'V',
            'min': 36.0,
            'max': 72.0,
            'step': 0.1
        },
        'batteryMaximumVoltage': {
            'number': 1121,
            'param': True,
            'component': 'number',
            'device_class': 'voltage',
            'unit_of_measurement': 'V',
            'min': 37.9,
            'max': 74.4,
            'step': 0.1
        },
        'floatingVoltage': {
            'number': 1140,
            'param': True,
            'component': 'number',
            'device_class': 'voltage',
            'unit_of_measurement': 'V',
            'min': 37.9,
            'max': 72.0,
            'step': 0.1
        },
        'forceFloatingPhase': {
            'number': 1467,
            'param': True,
            'component': 'switch',
        },
        'forceNewChargeCycle': {
            'number': 1142,
            'param': True,
            'component': 'switch',
        },
        'autoAcInputCurrentReduction': {
            'number': 1527,
            'param': True,
            'component': 'switch',
        },
        'boostPhaseAllowed': {
            'number': 1155,
            'param': True,
            'component': 'switch',
        },
        'boostVoltage': {
            'number': 1156,
            'param': True,
            'component': 'number',
            'device_class': 'voltage',
            'unit_of_measurement': 'V',
            'min': 37.9,
            'max': 72.0,
            'step': 0.1
        },
        'inputCurrentAdaptionRange': {
            'number': 1433,
            'param': True,
            'component': 'number',
            'device_class': 'current',
            'unit_of_measurement': 'A',
            'min': 4,
            'max': 30,
            'step': 1
        },

        'gridFeedingAllowed': {
            'number': 1127,
            'param': True,
            'component': 'switch',
        },
        'gridFeedingMaximumCurrent': {
            'number': 1523,
            'param': True,
            'component': 'number',
            'device_class': 'current',
            'unit_of_measurement': 'A',
            'min': 0.0,
            'max': 50.0,
            'step': 0.2
        },
        'gridFeedingBatteryVoltage': {
            'number': 1524,
            'param': True,
            'component': 'number',
            'device_class': 'voltage',
            'unit_of_measurement': 'V',
            'min': 37.9,
            'max': 72.0,
            'step': 0.1
        },
        'gridFeedingStartTime': {
            'number': 1525,
            'param': True,
            'component': 'number',
            'min': 0,
            'max': 1440,
            'step': 1
        },
        'gridFeedingStopTime': {
            'number': 1526,
            'param': True,
            'component': 'number',
            'min': 0,
            'max': 1440,
            'step': 1
        },
        'frequencyControlEnabled': {
            'number': 1627,
            'param': True,
            'component': 'switch',
        },
        'batteryPriorityAsEnergySource': {
            'number': 1296,
            'param': True,
            'component': 'switch',
        },
        'batteryPriorityVoltage': {
            'number': 1297,
            'param': True,
            'component': 'number',
            'device_class': 'voltage',
            'unit_of_measurement': 'V',
            'min': 37.9,
            'max': 72.0,
            'step': 0.1
        },
        'batteryVoltageToDeactivate': {
            "number": 1255,
            "param": True,
            'component': 'number',
            'device_class': 'voltage',
            'unit_of_measurement': 'V',
            'min': 36.0,
            'max': 77.0,
            'step': 0.1
        },
        'remoteEntryActivate': {
            "number": 1545,
            "param": True,
            'component': 'switch',
        },
        'operatingState': {
            'number': 3028,
            'param': False,
            'component': 'sensor',
            'device_class': None,
            'icon': None,
            'unit_of_measurement': None,
            'enum_map': {
                0: 'Invalid value',
                1: 'Inverter',
                2: 'Charger',
                3: 'Boost',
                4: 'Injection'
            }
        },
        'chargerAllowed': {
            "number": 1125,
            "param": True,
            'component': 'switch',
        },

    }
