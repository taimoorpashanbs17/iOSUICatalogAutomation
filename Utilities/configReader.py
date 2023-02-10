from configparser import ConfigParser
from Utilities.getpath import get_file_path

file_name = get_file_path('ConfigurationData', 'conf.ini')


def read_config(section, key):
    config = ConfigParser()
    config.read(file_name)
    return config.get(section, key)
