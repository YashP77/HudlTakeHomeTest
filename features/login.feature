@FunctionalTest
Feature: Test Login functionality
  As a user
  I want to be able to log in to my Hudl account
  So that I can access my personalized services

  Background:
    Given I am on the homepage
    And I go to the login page

  @SmokeTest @RegressionTest1.1
  Scenario Outline: Successful login with valid credentials
    When I enter valid email <email>
    And I enter valid password <password>
    And I click on the continue button
    Then I should be redirected to the dashboard

  Examples:
    | email                   | password     |
    | yash_patel1998@live.com | Password123. |

  @RegressionTest1.2
  Scenario Outline: Unsuccessful login with valid email and invalid password
    When I enter valid email <email>
    And I enter invalid password <invalidPassword>
    And I click on the continue button
    Then I should receive the correct error message

  Examples:
    | email                   | invalidPassword      |
    | yash_patel1998@live.com | Password123          |

  @RegressionTest1.3
  Scenario Outline: Unsuccessful login with invalid email and valid password
    When I enter invalid email <invalidEmail>
    And I enter valid password <password>
    And I click on the continue button
    Then I should receive the correct error message

  Examples:
    | invalidEmail   | password     |
    | yash_patel1998 | Password123. |


  @RegressionTest1.4
  Scenario: Unsuccessful login with empty email and password fields
    When I click on the continue button
    Then I should receive the correct error message


  @RegressionTest1.5
  Scenario: Check Forgot Password link redirect
    When I click on the Forgot Password link
    Then I should be redirected to the correct page

  @RegressionTest1.6
  Scenario: Check Create Account link redirect
    When I click on the Create Account link
    Then I should be redirected to the correct page

  @RegressionTest1.7
  Scenario Outline: Check Login with external account link redirect
    When I click on the continue with <accountType> link
    Then I should be redirected to the correct <accountType> login page

    Examples:
    | accountType |
    | Facebook    |
    | Google      |
    | Apple       |