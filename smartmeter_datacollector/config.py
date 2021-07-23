import configparser
import logging
from typing import List, Union


class InvalidConfigError(Exception):
    pass


DEFAULT_CONFIG = {
    'reader0': {
        'type': "lge450",
        'port': "/dev/ttyUSB0",
        'key': "",
    },
    'sink0': {
        'type': "logger",
        'name': "DataLogger",
    },
    'sink1': {
        'type': "mqtt",
        'host': "localhost",
    },
    'logging': {
        'default': 'DEBUG',
        'smartmeter': 'DEBUG',
        'sink': 'DEBUG',
    }
}


def read_config_files(config_paths: Union[str, List[str]]) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    read_files = config.read(config_paths)
    if read_files:
        logging.info("Read following config files: %s", read_files)
    else:
        logging.warning("No config file found. Using default config.")
        config = get_default_config()
    return config


def get_default_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read_dict(DEFAULT_CONFIG)
    return config


def write_default_config(config_path: str):
    config = get_default_config()
    with open(config_path, 'w') as file:
        config.write(file, True)