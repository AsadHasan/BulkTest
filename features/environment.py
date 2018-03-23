from configparser import ConfigParser

import os

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


def after_step(context, step):
    screenshots_directory = os.path.join(definitions.PROJECT_ROOT, "screenshots")
    if step.status == "failed":
        if not os.path.exists(screenshots_directory):
            os.makedirs(screenshots_directory)
        os.chdir(screenshots_directory)
        definitions.DRIVER.save_screenshot(step.name + ".png")


def after_all(context):
    definitions.DRIVER.quit()
