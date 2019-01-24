import pytest


@pytest.mark.usefixtures('driver')
class TestSample:

    def test_sample(self, driver):
        driver.get('https://www.google.com/ncr')
        assert "Google" == driver.title
