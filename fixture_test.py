
import pytest
from selenium.webdriver import Edge
from selene.support.shared import browser


@pytest.fixture
def open_demo():
    browser.config.driver = Edge()
    browser.config.window_height = 800
    browser.config.window_width = 1200
    browser.config.base_url = 'https://demoqa.com'
    browser.config.hold_browser_open = True
    browser.open('/automation-practice-form')
    yield browser

