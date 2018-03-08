from configparser import ConfigParser

import sys

sys.path.append("../")
from definitions import CONFIG_PATH


def before_all(context):
    parser = ConfigParser()
    parser.read(CONFIG_PATH)
    context.url = parser.get("Default", "baseUrl")
    context.browser = parser.get("Default", "browser")

