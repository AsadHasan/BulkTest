from pages.PageHelper import PageHelper
from pages.pageobjects.SearchResults import SearchResults


class SearchResultsChecks:
    def __init__(self, driver):
        self.driver = driver
        self.helper = PageHelper(self.driver)

    def checkLabels(self, label):
        if self.helper.elementsAvailable(*SearchResults.RESULT_LABELS):
            labelLists = self.driver.find_elements(*SearchResults.RESULT_LABELS)
            for labelList in labelLists:
                for element in labelList:
                    labelText=element.get_attribute("outerText")
                    print(labelText)
                    assert label in labelText
