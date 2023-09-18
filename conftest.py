import pytest
from selene import browser, have



@pytest.fixture(scope="session")
def open_browser():
    browser.open("https://www.google.com/")


@pytest.fixture(scope="session")
def setting_browser():
    browser.driver.set_window_size(499, 700)