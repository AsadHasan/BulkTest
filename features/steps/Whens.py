from behave import when

from pages.pageobjects.Homepage import Homepage


@when(u'I search for {text}')
def step_impl(context, text):
    print(text)
    Homepage(context.driver).searchFor(text)

@when(u'apply vegan on the results')
def step_impl(context):
    pass
