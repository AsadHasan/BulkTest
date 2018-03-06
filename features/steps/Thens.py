from behave import then

from pages.pagechecks.SearchResultsChecks import SearchResultsChecks


@then(u'only products with filter {label} are shown')
def step_impl(context, label):
    SearchResultsChecks(context.driver).checkLabels(label)