from selenium.webdriver.common.by import By

from pages.PageHelper import PageHelper


class Homepage:
    SEARCH_FIELD = (By.ID, "search")

    def __init__(self, driver):
        self.driver = driver

    def searchFor(self, text):
        PageHelper(self.driver).waitToBeClickable(*Homepage.SEARCH_FIELD)
        searchField = self.driver.find_element(*Homepage.SEARCH_FIELD)
        searchField.send_keys(text)
