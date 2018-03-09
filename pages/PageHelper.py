from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageHelper:
    def __init__(self, driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_to_be_clickable(self, *locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def elements_available(self, *locator):
        try:
            self.wait.until(expected_conditions.visibility_of_all_elements_located(locator))
            return True
        except TimeoutException:
            return False