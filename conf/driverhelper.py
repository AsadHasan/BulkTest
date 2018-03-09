from selenium import webdriver

import definitions
from definitions import CHROME_DRIVER_PATH, GECKO_DRIVER_PATH, IE_DRIVER_PATH


def set_driver(browser):
    if browser == "chrome":
        definitions.DRIVER = webdriver.Chrome(CHROME_DRIVER_PATH)

    elif browser == "firefox":
        definitions.DRIVER = webdriver.Firefox()

    elif browser == "edge":
        definitions.DRIVER = webdriver.Edge()

    else:
        print("Browser not supported")
