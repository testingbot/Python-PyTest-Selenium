## TestingBot - Python & PyTest

TestingBot provides an online grid of browsers and mobile devices to run automated tests on via Selenium WebDriver.
This example demonstrates how to use Python with [pytest](https://docs.pytest.org/) and [pytest-selenium](https://pytest-selenium.readthedocs.io/) to run tests on TestingBot.

### Requirements

* Python 3.9 or newer

### Environment Setup

1. Setup
    * Clone the repo
    * Install the dependencies: `pip install -r requirements.txt`

2. TestingBot Credentials
    * Add your TestingBot Key and Secret as environment variables. You can find these in the [TestingBot Dashboard](https://testingbot.com/members/).
    ```
    $ export TESTINGBOT_KEY=<your TestingBot Key>
    $ export TESTINGBOT_SECRET=<your TestingBot Secret>
    ```

### Running Tests

* Sample Test:
    ```
    $ pytest test_sample.py
    ```

`pytest.ini` selects the TestingBot driver and the browser (latest Chrome on Windows 11).
To use another browser, override a capability on the command line:

```
$ pytest test_sample.py --capability browserName firefox
```

pytest-selenium marks each test as passed or failed on TestingBot and prints a link to the test.
You will see the test result in the [TestingBot Dashboard](https://testingbot.com/members/).

### Resources
##### [TestingBot Documentation](https://testingbot.com/support/)

##### [Selenium Documentation](https://www.selenium.dev/documentation/)

##### [pytest-selenium Documentation](https://pytest-selenium.readthedocs.io/en/latest/index.html)
