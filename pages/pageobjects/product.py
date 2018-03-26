from selenium.webdriver.common.by import By

import definitions

DESCRIPTION = (By.ID, "nav-description")
ADD_TO_CART_BUTTON = (By.ID, "product-addtocart-button")
QUANTITY_BUTTON = (By.ID, "qty")
CART_ADDITION_SUCCESS_MESSAGE = (By.CLASS_NAME, "product-popup-content")
CHECKOUT_BUTTON = (By.XPATH, "//*[text()='Checkout']")


def add_to_cart(*quantity):
    if quantity:
        definitions.HELPER.wait_to_be_clickable(*QUANTITY_BUTTON)
        definitions.DRIVER.find_element(*QUANTITY_BUTTON).send_keys(quantity)
    definitions.HELPER.wait_to_be_clickable(*ADD_TO_CART_BUTTON)
    definitions.DRIVER.find_element(*ADD_TO_CART_BUTTON).click()


def checkout(product):
    if product_in_cart(product):
        definitions.HELPER.wait_to_be_clickable(*CHECKOUT_BUTTON)
        definitions.DRIVER.find_element(*CHECKOUT_BUTTON).click()


def product_in_cart(product):
    expected_message = "You added " + product + " to your shopping cart."
    definitions.HELPER.wait_to_be_clickable(*CART_ADDITION_SUCCESS_MESSAGE)
    actual_message = definitions.DRIVER.find_element(*CART_ADDITION_SUCCESS_MESSAGE).text

    if expected_message in actual_message:
        return True
    else:
        return False


def product_has_description():
    definitions.HELPER.wait_to_be_clickable(*DESCRIPTION)
    description = definitions.DRIVER.find_element(*DESCRIPTION)

    if description.get_attribute("outerText"):
        return True
    else:
        return False
