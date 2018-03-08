from selenium import webdriver
from definitions import CHROME_DRIVER_PATH, GECKO_DRIVER_PATH, IE_DRIVER_PATH


class DriverHelper:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

        elif browser == "firefox":
            self.driver = webdriver.Firefox()

        elif browser == "edge":
            self.driver = webdriver.Edge()

        else:
            print("Browser not supported")
