import logging
from typing import Optional, List
from playwright.sync_api import Page, expect
import re

from framework_playwright.playwright.pages.base_page import BasePage

logger = logging.getLogger(__name__)

class HomePage(BasePage):
    path = ""

    EXPECTED_CARDS = [
        'Elements',
        'Forms',
        'Alerts, Frame & Windows',
        'Widgets',
        'Interactions',
        'Book Store Application'
    ]

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.navigate_to(self.path)
        expect(self.page.locator(".home-banner")).to_be_visible()

    def verify_banner_visible(self):
        home_banner = self.page.locator("img[alt='Selenium Online Training']")
        expect(home_banner).to_be_visible()

    def verify_cards(self, expected_cards: Optional[List[str]] = None) -> bool:

        expected_cards = expected_cards or self.EXPECTED_CARDS

        card_names = self.page.locator(".card-body").all_inner_texts()
        for raw_name in card_names:
            name = raw_name.split("\n")[0].strip()
            print(f"Verifying card: {name}")
            assert name in expected_cards, f"{name} not found in expected cards"


        print("All card names verified successfully.")
        return True

