# features/steps/web_steps.py

from behave import when, then

@when('I visit the "home page"')
def step_impl(context):
    context.driver.get(context.base_url)

@when('I set the "{field}" field to "{value}"')
def step_impl(context, field, value):
    element = context.driver.find_element_by_name(field)
    element.clear()
    element.send_keys(value)

@when('I press the "{button}" button')
def step_impl(context, button):
    button = context.driver.find_element_by_xpath(f"//button[text()='{button}']")
    button.click()

@then('I should see "{message}"')
def step_impl(context, message):
    assert message in context.driver.page_source
