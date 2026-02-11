from playwright.sync_api import Playwright

from framework_playwright.playwright.pages.home import HomePage


def test_homepage(browser_instance):
    home_page = HomePage(browser_instance)
    home_page.open()
    home_page.verify_banner_visible()
    home_page.verify_cards()



