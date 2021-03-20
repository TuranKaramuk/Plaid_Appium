Feature: Test for Plaid Toolbar

  Scenario: Search Button Displayed On Startup
    Given The app is first launched
    Then  The Search button should be displayed

  Scenario: Login in to Designer News Displayed On Overflow More Options Pressed
    Given The app is first launched
    When More option button pressed
    Then Verify Login in to Designer News displayed in more options

  Scenario: About Displayed On Overflow More Options Pressed
    Given The app is first launched
    When More option button pressed
    Then Verify About displayed in more options