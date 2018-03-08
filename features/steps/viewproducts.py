from behave import given, when, then


@given(u'I am presented search results for {term}')
def step_impl(context, term):
    context.execute_steps(u"""
        given I am on the homepage
        when I search for {products}
    """.format(products=term))


@when(u'I select a SHAKER BOTTLE BLACK 700ML')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select a PRO SERIES™ STORAGE SHAKER™ 600ML')


@then(u'I can view the product details')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can view the product details')
