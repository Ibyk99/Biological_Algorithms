#############################################################
# See https://docs.python.org/3/library/configparser.html   #
# Holds the main settings for the applications              #
#############################################################

import configparser

settings = configparser.ConfigParser(allow_no_value=True)

def read(file="settings.ini"):
    global settings
    with open(file) as fh:
        settings.read_file(fh)


def write(file="settings.ini"):
    global settings

    with open(file, 'w') as configfile:
        settings.write(configfile)