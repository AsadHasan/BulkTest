from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import definitions
from definitions import CHROME_DRIVER_PATH, GECKO_DRIVER_PATH, IE_DRIVER_PATH


def set_driver(browser):
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        definitions.DRIVER = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_DRIVER_PATH)

    elif browser == "firefox":
        definitions.DRIVER = webdriver.Firefox()

    elif browser == "edge":
        definitions.DRIVER = webdriver.Edge()

    else:
        print("Browser not supported")
