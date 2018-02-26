from behave import then

from pages.pagechecks.SearchResultsChecks import SearchResultsChecks


@then(u'only products with filter {text} are shown')
def step_impl(context, text):
    SearchResultsChecks(context.driver).checkLabels(text)