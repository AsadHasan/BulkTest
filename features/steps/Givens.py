from behave import given

from conf.DriverHelper import DriverHelper


@given(u'I am on the homepage')
def step_impl(context):
    context.driver=DriverHelper(context.browser,context.driverPath).driver
    context.driver.maximize_window()
    context.driver.get(context.url)
