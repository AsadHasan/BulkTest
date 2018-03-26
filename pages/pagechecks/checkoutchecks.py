from pages.pageobjects.checkout import can_proceed_to_checkout


def check_option_to_checkout():
    assert can_proceed_to_checkout()