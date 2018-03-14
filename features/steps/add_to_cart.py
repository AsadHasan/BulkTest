from behave import given, when, then

from pages.pageobjects.product import add_to_cart


@given(u'I select a {product}')
def step_impl(context, product):
    context.execute_steps(u"""
        given I am presented search results for {product}
        when I select a {product}
    """.format(product=product))


@when(u'I add it to shopping cart')
def step_impl(context):
    add_to_cart();


@then(u'it is successfully added to the shopping cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it is successfully added to the shopping cart')
