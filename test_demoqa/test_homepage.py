from playwright.sync_api import Playwright

from pages_demoqa.home.home_page import HomePage


def test_homepage(playwright: Playwright, browser_instance):
    home_page = HomePage(browser_instance)
    home_page.open()
    home_page.verify_banner_visible()
    home_page.verify_cards()



