from selenium.webdriver.common.by import By

from pages.PageHelper import PageHelper


class Homepage:
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BUTTON=(By.CSS_SELECTOR, "button[title=Search]")

    def __init__(self, driver):
        self.driver = driver
        self.helper=PageHelper(self.driver)

    def searchFor(self, text):
        self.helper.waitToBeClickable(*Homepage.SEARCH_FIELD)
        self.driver.find_element(*Homepage.SEARCH_FIELD).send_keys(text)
        self.helper.waitToBeClickable(*Homepage.SEARCH_BUTTON)
        self.driver.find_element(*Homepage.SEARCH_BUTTON).click()
