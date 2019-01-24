[![Build Status](https://travis-ci.org/testingbot/Python-Pytest-Selenium.svg?branch=master)](https://travis-ci.org/testingbot/Python-Pytest-Selenium)

## TestingBot - Python & PyTest

TestingBot provides an online grid of browsers and mobile devices to run Automated tests on via Selenium WebDriver.
This example demonstrates how to use Python with PyTest to run tests across several browsers.

### Environment Setup
1. Setup
    * Clone the repo
    * Install the dependencies `pip install -r requirements.txt`

2. TestingBot Credentials
    * Add your TestingBot Key and Secret as environmental variables. You can find these in the [TestingBot Dashboard](https://testingbot.com/members/).
    ```
    $ export TESTINGBOT_KEY=<your TestingBot Key>
    $ export TESTINGBOT_SECRET=<your TestingBot Secret>
    ```

### Running Tests

* Sample Test:
    ```
    $ pytest test_sample.py
    ```
You will see the test result in the [TestingBot Dashboard](https://testingbot.com/members/)

### Resources
##### [TestingBot Documentation](https://testingbot.com/support/)

##### [SeleniumHQ Documentation](http://www.seleniumhq.org/docs/)

##### [PyTest Documentation](https://pytest-selenium.readthedocs.io/en/latest/index.html)
