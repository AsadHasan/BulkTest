import definitions
from pages.pageobjects.searchresults import RESULT_LABELS


def check_labels(expectedLabel):
    if definitions.HELPER.elements_available(*RESULT_LABELS):
        labelsList = definitions.DRIVER.find_elements(*RESULT_LABELS)
        for label in labelsList:
            actualLabel = label.get_attribute("outerText")
            assert expectedLabel in actualLabel
