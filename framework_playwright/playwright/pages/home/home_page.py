import logging
from typing import Optional, List
from playwright.sync_api import Page, expect


from framework_playwright.playwright.pages.base_page import BasePage

logger = logging.getLogger(__name__)

class HomePage(BasePage):
    path = ""

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @property
    def card_type_loc(self):
        """Return all locators for all card types"""
        return self.page.locator(".card-body h5")

    @property
    def home_page_banner_loc(self):
        """Return Home Page Banner locator"""
        return self.page.locator("img[alt='Selenium Online Training']")

    def open(self):
        super().open_page(self.path)



