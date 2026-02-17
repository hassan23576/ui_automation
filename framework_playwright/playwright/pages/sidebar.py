import re

import logging
from playwright.sync_api import Page, expect

from framework_playwright.playwright.pages.base_page import BasePage

logger = logging.getLogger(__name__)

class Sidebar(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def element_group(self, element_text: str):
        return self.page.locator(".element-group").filter(has_text=element_text)


    def select_side_bar_option(self, element_text, item_text: str, expected_title: bool = True):
        """Click a menu item on the left panel by visible text."""
        header = self.element_group(element_text).locator(".header-text")
        element_list = self.element_group(element_text).locator(".element-list.collapse.show")
        text_center = self.page.locator(".text-center")
        is_open = element_list.is_visible()
        if not is_open:
            logger.info(f"Expand elements list: {element_text}")
            header.click()
            try:
                expect(element_list).to_be_visible()
            except AssertionError:
                raise Exception(f"Failed to expand elements Sidebar: '{element_text}'. Menu list is not visible.")
        self.select_menu_item(item_text)
        if expected_title:
            text_center.wait_for(timeout=5000)
            return text_center.inner_text()
        else:
            logger.info(f"Title not expected for menu item: {item_text}")
        return None



