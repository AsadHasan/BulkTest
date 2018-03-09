from configparser import ConfigParser

import definitions
from conf.driverhelper import set_driver
from definitions import CONFIG_PATH
from pages.PageHelper import PageHelper


def before_all(context):
    parser = ConfigParser()
    parser.read(CONFIG_PATH)
    context.url = parser.get("Default", "baseUrl")
    context.browser = parser.get("Default", "browser")
    set_driver(context.browser)
    context.helper = PageHelper(definitions.DRIVER)
    definitions.HELPER = context.helper

def after_all(context):
    definitions.DRIVER.quit()
