from behave import given, when, then

from pages.pagechecks.checkoutchecks import check_option_to_checkout
from pages.pageobjects.product import checkout


@given(u'I have added {product} to cart')
def step_impl(context, product):
    context.execute_steps(u"""
        given I select a {product}
        when I add it to shopping cart
    """.format(product=product))
    context.product = product


@when(u'I choose to checkout')
def step_impl(context):
    checkout(context.product)


@then(u'I should be provided the option to checkout with my purchase')
def step_impl(context):
    check_option_to_checkout()
