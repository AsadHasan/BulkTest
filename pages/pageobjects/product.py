from selenium.webdriver.common.by import By

import definitions

DESCRIPTION = (By.ID, "nav-description")


def product_has_description():
    definitions.HELPER.wait_to_be_clickable(*DESCRIPTION)
    description = definitions.DRIVER.find_element(*DESCRIPTION)

    if description.get_attribute("outerText"):
        return True
    else:
        return False
