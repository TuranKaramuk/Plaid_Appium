from behave import given, when, then


@given('The app is first launched')
def step_impl(context):
    pass

@then('The search button should be displayed')
def step_impl(context):
    context.app.main_page.verify_search_icon()


@when('More option button pressed')
def step_impl(context):
    context.app.main_page.tap_more_options()


@then('Verify About displayed in more options')
def verify_about_displayed(context):
    context.app.main_page.verify_about_displayed()

@then('Verify Login in to Designer News displayed in more options')
def verify_about_displayed(context):
    context.app.main_page.verify_log_in_to_designer_news_displayed()
