from behave import given, when, then

from pages.pagechecks.productchecks import check_product_added_to_cart
from pages.pageobjects.product import add_to_cart


@given(u'I select a {product}')
def step_impl(context, product):
    context.execute_steps(u"""
        given I am presented search results for {product}
        when I select a {product}
    """.format(product=product))
    context.product=product


@when(u'I add it to shopping cart')
def step_impl(context):
    add_to_cart();


@then(u'it is successfully added to the shopping cart')
def step_impl(context):
    check_product_added_to_cart(context.product)
