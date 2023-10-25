Feature: Test Login functionality
  As a user
  I want to be able to log in to my Hudl account
  So that I can access my personalized services

  Background:
    Given I am on the homepage
    And I go to the login page


  Scenario Outline: Successful login with valid credentials
    When I enter valid email <email>
    And I enter valid password <password>
    And I click on the continue button
    Then I should be redirected to the dashboard

  Examples:
    | email                   | password     |
    | yash_patel1998@live.com | Password123. |


  Scenario Outline: Unsuccessful login with valid email and invalid password
    When I enter valid email <email>
    And I enter invalid password <invalidPassword>
    And I click on the continue button
    Then I should receive an error message

  Examples:
    | email                   | invalidPassword      |
    | yash_patel1998@live.com | Password123          |


  Scenario Outline: Unsuccessful login with invalid email and valid password
    When I enter invalid email <invalidEmail>
    And I enter valid password <password>
    And I click on the continue button
    Then I should receive an error message

  Examples:
    | invalidEmail   | password     |
    | yash_patel1998 | Password123. |
