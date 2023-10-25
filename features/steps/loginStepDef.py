from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


@given('I am on the homepage')
def step_impl(context):
    driver.get("https://www.hudl.com")


@given('I go to the login page')
def step_impl(context):
    driver.find_element(By.PARTIAL_LINK_TEXT, "Log in").click()
    # Revisit before submission
    driver.find_element(By.XPATH, "//div[1]/header/div/div/div/div/div[1]").click()


@when("I enter valid email {email}")
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    :type email: str
    """
    driver.find_element(By.ID, "email").send_keys(email)


@step("I enter valid password {password}")
def step_impl(context, password):
    """
    :type context: behave.runner.Context
    :type password: str
    """
    driver.find_element(By.ID, "password").send_keys(password)


@step("I click on the continue button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.find_element(By.ID, "logIn").click()


@then("I should be redirected to the dashboard")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    time.sleep(1)
    navBarExists = driver.find_element(By.ID, "ssr-webnav").is_displayed()

    assert navBarExists
    driver.quit()