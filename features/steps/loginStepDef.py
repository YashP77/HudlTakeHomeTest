from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


@given('I am on the homepage')
def step_impl(context):
    time.sleep(5)
    driver.get("https://www.hudl.com")


@given('I go to the login page')
def step_impl(context):
    driver.find_element(By.PARTIAL_LINK_TEXT, "Log in").click()
    # Revisit before submission
    driver.find_element(By.XPATH, "//div[1]/header/div/div/div/div/div[1]").click()


@when("I enter valid email {email}")
def step_impl(context, email):
    driver.find_element(By.ID, "email").send_keys(email)


@step("I enter valid password {password}")
def step_impl(context, password):
    driver.find_element(By.ID, "password").send_keys(password)


@step("I click on the continue button")
def step_impl(context):
    driver.find_element(By.ID, "logIn").click()


@then("I should be redirected to the dashboard")
def step_impl(context):
    time.sleep(1)
    navBarExists = driver.find_element(By.ID, "ssr-webnav").is_displayed()

    assert navBarExists, "Dashboard not found"
    driver.quit()


@step("I enter invalid password {invalidPassword}")
def step_impl(context, invalidPassword):
    driver.find_element(By.ID, "password").send_keys(invalidPassword)


@then("I should receive the correct error message")
def step_impl(context):
    time.sleep(3)

    if 'RegressionTest1.4' in context.tags:
        missingInfoErrorMsgExists = driver.find_element(By.ID, "uniName_947Help").is_displayed()
        assert missingInfoErrorMsgExists, "Missing information error message not found"
    else:
        errorMsgExists = driver.find_element(By.CSS_SELECTOR, ".error-container").is_displayed()
        assert errorMsgExists, "Error message not found"

    driver.quit()


@when("I enter invalid email {invalidEmail}")
def step_impl(context, invalidEmail):
    driver.find_element(By.ID, "email").send_keys(invalidEmail)


@when("I click on the forgot password link")
def step_impl(context):
    driver.find_element(By.LINK_TEXT, "Forgot Password").click()


@then("I should be redirected to the correct page")
def step_impl(context):
    time.sleep(5)

    if 'RegressionTest1.5' in context.tags:
        forgotPasswordPageExists = driver.find_element(By.ID, "email-reset-container").is_displayed()
        assert forgotPasswordPageExists, "Forgot Password page not found"
    elif 'RegressionTest1.6' in context.tags:
        createAccountPageExists = driver.find_element(By.ID, "signup-box").is_displayed()
        assert createAccountPageExists, "Create Account page not found"

    driver.quit()


@when("I click on the Create Account link")
def step_impl(context):
    driver.find_element(By.ID, "btn-show-signup").click()


@when("I click on the continue with {accountType} link")
def step_impl(context, accountType):
    if accountType == "Facebook":
        driver.find_element(By.ID, "btn-facebook-login").click()
    elif accountType == "Google":
        driver.find_element(By.ID, "btn-google-login").click()
    elif accountType == "Apple":
        driver.find_element(By.ID, "btn-apple-login").click()


@then("I should be redirected to the correct {accountType} login page")
def step_impl(context, accountType):
    if accountType == "Facebook":
        facebook_login_link = str(driver.current_url)
        assert "facebook.com/login" in facebook_login_link, "Facebook login page not found"
    elif accountType == "Google":
        google_login_link = str(driver.current_url)
        assert "accounts.google.com/" in google_login_link, "Google login page not found"
    elif accountType == "Apple":
        apple_login_link = str(driver.current_url)
        assert "appleid.apple.com/" in apple_login_link, "Apple login page not found"

    driver.quit()
