from selenium.webdriver.common.by import By

import definitions

CHECKOUT_BUTTON=(By.CSS_SELECTOR,"[data-role=proceed-to-checkout]")

def can_proceed_to_checkout():
    definitions.HELPER.elements_available(*CHECKOUT_BUTTON)