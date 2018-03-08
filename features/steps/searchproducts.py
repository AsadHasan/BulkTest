from behave import given
from conf.DriverHelper import DriverHelper
from behave import when
from pages.pageobjects.Homepage import Homepage
from pages.pageobjects.SearchResults import SearchResults
from behave import then
from pages.pagechecks.SearchResultsChecks import SearchResultsChecks


@given(u'I am on the homepage')
def step_impl(context):
    context.driver = DriverHelper(context.browser).driver
    context.driver.maximize_window()
    context.driver.get(context.url)


@when(u'I search for {products}')
def step_impl(context, products):
    Homepage(context.driver).searchFor(products)


@when(u'apply {filter} on the results')
def step_impl(context, filter):
    SearchResults(context.driver).filterResultsBy(filter)


@then(u'only products with filter {label} are shown')
def step_impl(context, label):
    SearchResultsChecks(context.driver).checkLabels(label)
