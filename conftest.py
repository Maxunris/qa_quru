import pytest
from selene import browser, have


@pytest.fixture(scope="session")
def open_browser():
    browser.open("https://www.google.com/")


@pytest.fixture(scope="session")
def setting_browser():
    browser.should(have.size_greater_than(5))
