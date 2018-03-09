from selenium.webdriver.common.by import By

import definitions

SEARCH_FIELD = (By.ID, "search")
SEARCH_BUTTON = (By.CSS_SELECTOR, "button[title=Search]")


def search_for(text):
    definitions.HELPER.wait_to_be_clickable(*SEARCH_FIELD)
    definitions.DRIVER.find_element(*SEARCH_FIELD).send_keys(text)
    definitions.HELPER.wait_to_be_clickable(*SEARCH_BUTTON)
    definitions.DRIVER.find_element(*SEARCH_BUTTON).click()
