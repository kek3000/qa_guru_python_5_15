"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(params=[(1680, 1050), (1920, 1080)])
def web_browser_for_desktop(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.window_height = request.param[1]
    browser.config.window_width = request.param[0]
    yield browser
    browser.quit()


@pytest.fixture(params=[(375, 667), (390, 844)])
def web_browser_for_mobile(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.window_height = request.param[1]
    browser.config.window_width = request.param[0]
    yield browser
    browser.quit()


def test_github_desktop(web_browser_for_desktop):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(web_browser_for_mobile):
    browser.open("https://github.com/")
    browser.element('.Button--link.Button--medium').click()
    browser.element('.HeaderMenu-link--sign-in').click()
