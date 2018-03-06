from pages.PageHelper import PageHelper
from pages.pageobjects.SearchResults import SearchResults


class SearchResultsChecks:
    def __init__(self, driver):
        self.driver = driver
        self.helper = PageHelper(self.driver)

    def checkLabels(self, expectedLabel):
        if self.helper.elementsAvailable(*SearchResults.RESULT_LABELS):
            labelsList = self.driver.find_elements(*SearchResults.RESULT_LABELS)
            for label in labelsList:
                actualLabel = label.get_attribute("outerText")
                assert expectedLabel in actualLabel
      