import pytest


@pytest.mark.usefixtures('driver')
class TestSample:

    def test_sample(self, driver):
        driver.get('https://testingbot.com')
        assert 'TestingBot' in driver.title
