import os

import logging
import re

from playwright.sync_api import Page, expect, Locator
from typing import Any

logger = logging.getLogger(__name__)

class BasePage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate_to(self, path: str):
        self.page.goto(path, wait_until="domcontentloaded")

    def open_page(self, path, expected_title=None):
        logger.info(f"Opening page: {self.base_url}{path}")
        self.navigate_to(path)
        expect(self.page).to_have_url(re.compile(f".*{self.base_url}{path}"))
        self.expected_title(expected_title)


    def handle_ad_popup(self):
        google_ad = self.page.locator('#close-fixedban')
        if google_ad.is_visible(timeout=200):
            google_ad.evaluate("node => node.remove()")

    @staticmethod
    def force_js_click(locator: Locator):
        locator.evaluate("node => node.click()")

    @staticmethod
    def enter_text(locator: Locator, value: Any, delay: int = 0):
        text_value = str(value)
        locator.wait_for(state="visible")

        if delay > 0:
            locator.press_sequentially(text_value, delay=delay)
        else:
            locator.fill(text_value)

    @staticmethod
    def press_key(locator: Locator, key: str):
        locator.press(key)


    @staticmethod
    def upload_file(locator: Locator, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        locator.set_input_files(file_path)

    @staticmethod
    def verify_text(locator: Locator, text: str, timeout: int = 5000):
        expect(locator).to_contain_text(text, timeout=timeout)

    def expected_title(self, expected_title=None):
        if expected_title:
            self.verify_text(self.page.locator(".text-center"), expected_title)
        else:
            logger.info(f"No expected title provided, skipping title verification")

    def take_screenshot(self, name: str = "failure.png"):
        # Ensure the directory exists first so the test doesn't crash
        os.makedirs("screenshots", exist_ok=True)
        self.page.screenshot(path=f"screenshots/{name}", full_page=True)

    def navigate_to_section(self, section_name: str):
        self.handle_ad_popup()
        target = self.page.locator(".card-body", has_text=section_name)
        logger.info(f"Navigating to section: {section_name}")
        self.force_js_click(target)

    def select_menu_item(self, item_name: str):
        menu_list = self.page.locator(".left-pannel .menu-list span").get_by_text(item_name, exact=True)
        self.force_js_click(menu_list)
        menu_list.wait_for(state="visible")
        logger.info(f"Attempting to click on menu item: '{item_name}'")
        menu_list.click()






