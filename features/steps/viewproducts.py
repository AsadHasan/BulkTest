from behave import given, when, then

from pages.pagechecks.productchecks import check_product_details
from pages.pageobjects.searchresults import view_product


@given(u'I am presented search results for {term}')
def step_impl(context, term):
    context.execute_steps(u"""
        given I am on the homepage
        when I search for {products}
    """.format(products=term))


@when(u'I select a {product}')
def step_impl(context, product):
    view_product(product)


@then(u'I can view the product details')
def step_impl(context):
    check_product_details()
