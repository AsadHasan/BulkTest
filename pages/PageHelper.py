from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageHelper:
    def __init__(self, driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 15)

    def waitToBeClickable(self, *locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))

