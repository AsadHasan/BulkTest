from selenium.webdriver.common.by import By

from pages.PageHelper import PageHelper


class SearchResults:
    RESULT_LABELS = (By.CSS_SELECTOR, (".product-suitability"))

    def __init__(self, driver):
        self.driver = driver
        self.helper = PageHelper(self.driver)

    def filterResultsBy(self, filter):
        filterLocator = (By.CSS_SELECTOR, "[data-facet-value=" + filter + "]")
        moreOptionLocator = (By.CSS_SELECTOR, "[data-tb-test=\"Show more options\"]")

        if self.helper.elementsAvailable(*filterLocator):
            self.driver.find_element(*filterLocator).click()
        else:
            self.helper.waitToBeClickable(*moreOptionLocator)
            self.driver.find_element(*moreOptionLocator).click()
            self.helper.waitToBeClickable(*filterLocator)
            self.driver.find_element(*filterLocator).click()

