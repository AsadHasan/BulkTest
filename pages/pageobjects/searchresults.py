from selenium.webdriver.common.by import By

import definitions

RESULT_LABELS = (By.CSS_SELECTOR, (".product-suitability"))


def filter_results_by(filter):
    filterLocator = (By.CSS_SELECTOR, "[data-facet-value=" + filter + "]")
    moreOptionLocator = (By.CSS_SELECTOR, "[data-tb-test=\"Show more options\"]")

    if definitions.HELPER.elements_available(*filterLocator):
        definitions.DRIVER.find_element(*filterLocator).click()
    else:
        definitions.HELPER.wait_to_be_clickable(*moreOptionLocator)
        definitions.DRIVER.find_element(*moreOptionLocator).click()
        definitions.HELPER.wait_to_be_clickable(*filterLocator)
        definitions.DRIVER.find_element(*filterLocator).click()


def view_product(product):
    resultLocator = (By.XPATH, ("//*[text()='\n    " + product + "']"))
    definitions.HELPER.wait_to_be_clickable(*resultLocator)
    definitions.DRIVER.find_element(*resultLocator).click()
