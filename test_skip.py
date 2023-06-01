"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1680, 1050), (375, 667), (390, 844)],
                ids=['desktop', 'desktop', 'mobile', 'mobile'])
def browsers(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.window_height = request.param[1]
    browser.config.window_width = request.param[0]

    if 'desktop' in request.node.name and 'mobile' in request.node.callspec.id:
        pytest.skip('Для теста не подходит мобильное соотношение сторон')
    elif 'mobile' in request.node.name and 'desktop' in request.node.callspec.id:
        pytest.skip('Для теста не подходит десктопное соотношение сторон')

    yield browser
    browser.quit()


def test_github_desktop(browsers):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browsers):
    browser.open("https://github.com/")
    browser.element('.Button--link.Button--medium').click()
    browser.element('.HeaderMenu-link--sign-in').click()
