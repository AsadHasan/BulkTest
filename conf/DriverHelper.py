from selenium import webdriver


class DriverHelper:
    def __init__(self, browser, driverPath):
        if browser == "chrome":
            self.driver = webdriver.Chrome(driverPath)

        elif browser == "firefox":
            self.driver = webdriver.Firefox()

        elif browser == "edge":
            self.driver = webdriver.Edge()

        else:
            print("Browser not supported")
