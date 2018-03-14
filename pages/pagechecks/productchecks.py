from pages.pageobjects.product import product_has_description, product_in_cart


def check_product_details():
    assert product_has_description()

def check_product_added_to_cart(product):
    assert product_in_cart(product)

