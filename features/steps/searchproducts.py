from behave import given
from behave import when
from behave import then

import definitions
from pages.pagechecks.searchresultschecks import check_labels
from pages.pageobjects.homepage import search_for
from pages.pageobjects.searchresults import filter_results_by


@given(u'I am on the homepage')
def step_impl(context):
    definitions.DRIVER.maximize_window()
    definitions.DRIVER.get(context.url)


@when(u'I search for {products}')
def step_impl(context, products):
    search_for(products)


@when(u'apply {filter} on the results')
def step_impl(context, filter):
    filter_results_by(filter)


@then(u'only products with filter {label} are shown')
def step_impl(context, label):
    check_labels(label)
