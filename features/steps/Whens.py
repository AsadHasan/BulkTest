from behave import when

from pages.pageobjects.Homepage import Homepage
from pages.pageobjects.SearchResults import SearchResults


@when(u'I search for {text}')
def step_impl(context, text):
    Homepage(context.driver).searchFor(text)


@when(u'apply {text} on the results')
def step_impl(context, text):
    SearchResults(context.driver).filterResultsBy(text)
