import logging
import re

from playwright.sync_api import Page, expect

from framework_playwright.playwright.pages.base_page import BasePage

logger = logging.getLogger(__name__)

class NestedFramesPage(BasePage):
    path = "/nestedframes"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @property
    def parent_frame(self):
        return self.page.frame_locator("#frame1").locator("body")

    @property
    def child_frame(self):
        return self.page.frame_locator("#frame1").frame_locator("iframe[srcdoc*='Child']").locator("body")


    def open(self):
        super().open_page(self.path, "Nested Frames")

