# HudlTakeHomeTest

## Overview
This is a simple test automation framework for the Hudl login webpage. It is designed to run on Chrome, but can be easily extended to run on other browsers.

### Prerequisites and download links
* Python 3.12
  * https://www.python.org/downloads/
* Selenium
  * https://pypi.org/project/selenium/
* Behave
  * https://behave.readthedocs.io/en/stable/install.html

### Running the tests
Feature file is found within the features directory and the step definitions with implementation are found within the feature/steps directory

To run the tests, navigate to the root directory of the project and run the following command:
```behave```

Tests can also be run using preferred python IDE providing all prerequisites are met.

On windows I have encountered some issues with running the all the tests with the above command so if any issues are encountered I would recommend running the test tags individually by navigating to the features directory and running the command ```behave login.feature --tags=<tag>```.

I will list the tags below with the scenario that they run:
* @SmokeTest or @RegressionTest1.1
  * Successful login with valid credentials
* @RegressionTest1.2
  * Unsuccessful login with valid email and invalid password
* @RegressionTest1.3
  * Unsuccessful login with invalid email and valid password
* @RegressionTest1.4
  * Unsuccessful login with empty email and password fields
* @RegressionTest1.5
  * Check Forgot Password link redirect
* @RegressionTest1.6
  * Check Create Account link redirect
* @RegressionTest1.7
  * Check Login with external account link redirect

### Improvements
* I would like to have added more tests to cover different browsers and different operating systems to ensure cross browser and cross platform compatibility.
* I would have like to figure out why the all scenarios on the feature file with the behave command on windows which hinders the full automation of the tests.
* I also would have liked to include testing the login of external accounts such as Google and Facebook, to ensure users are taken to the right page after logging in externally
