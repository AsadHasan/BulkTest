from pages.pageobjects.product import product_has_description


def check_product_details():
    assert product_has_description()
