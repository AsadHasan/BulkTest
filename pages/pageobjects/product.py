from selenium.webdriver.common.by import By

import definitions

DESCRIPTION = (By.ID, "nav-description")
ADD_TO_CART_BUTTON = (By.ID, "product-addtocart-button")
QUANTITY_BUTTON = (By.ID, "qty")


def add_to_cart(*quantity):
    if quantity:
        definitions.HELPER.wait_to_be_clickable(*QUANTITY_BUTTON)
        definitions.DRIVER.find_element(*QUANTITY_BUTTON).send_keys(quantity)
    definitions.HELPER.wait_to_be_clickable(*ADD_TO_CART_BUTTON)
    definitions.DRIVER.find_element(*ADD_TO_CART_BUTTON).click()


def product_has_description():
    definitions.HELPER.wait_to_be_clickable(*DESCRIPTION)
    description = definitions.DRIVER.find_element(*DESCRIPTION)

    if description.get_attribute("outerText"):
        return True
    else:
        return False
