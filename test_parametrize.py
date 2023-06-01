"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(params=["desktop", "mobile"])
def browsers(request):
    if request.param == "desktop":
        browser.config.window_width = '1920'
        browser.config.window_height = '1080'
    if request.param == "mobile":
        browser.config.window_width = '390'
        browser.config.window_height = '844'
    yield browser
    browser.quit()


@pytest.mark.parametrize("browsers", ["desktop"], indirect=True)
def test_github_desktop(browsers):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize("browsers", ["mobile"], indirect=True)
def test_github_mobile(browsers):
    browser.open("https://github.com/")
    browser.element('.Button--link.Button--medium').click()
    browser.element('.HeaderMenu-link--sign-in').click()
