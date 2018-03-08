from behave import when

from pages.pageobjects.Homepage import Homepage
from pages.pageobjects.SearchResults import SearchResults


@when(u'I search for {products}')
def step_impl(context, products):
    Homepage(context.driver).searchFor(products)


@when(u'apply {filter} on the results')
def step_impl(context, filter):
    SearchResults(context.driver).filterResultsBy(filter)
