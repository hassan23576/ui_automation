import logging
from playwright.sync_api import expect

from framework_playwright.playwright.pages.home import HomePage
logger= logging.getLogger(__name__)

def test_homepage(page, base_url):
    logger.info(f"--- Running Home Page Test ---")
    home_page = HomePage(page, base_url)
    home_page.open()
    expect(home_page.home_page_banner_loc).to_be_visible()
    expected_cards = \
        ["Elements", "Forms", "Alerts, Frame & Windows", "Widgets", "Interactions", "Book Store Application"]
    expect(home_page.card_type_loc).to_have_text(expected_cards)



