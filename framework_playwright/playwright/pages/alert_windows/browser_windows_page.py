import logging
import re

from playwright.sync_api import expect, Page
from framework_playwright.playwright.pages.base_page import BasePage

logger = logging.getLogger(__name__)

class BrowserWindowsPage(BasePage):
    path = "/browser-windows"

    def __init__(self, page, base_url):
        super().__init__(page, base_url)

    @property
    def new_tab_btn(self):
        return self.page.locator("#tabButton")

    @property
    def new_window_btn(self):
        return self.page.locator("#windowButton")

    @property
    def new_message_window_btn(self):
        return self.page.locator("#messageWindowButton")

    @property
    def simple_heading_id(self):
        return self.page.locator("#simpleHeading")


    def open(self):
        logger.info(f"Opening Browser Windows page: {self.base_url}{self.path}")
        self.navigate_to(self.path)
        expect(self.page).to_have_url(re.compile(f".*{self.path}$"))
        self.verify_text(self.page.locator(".text-center"), "Browser Windows")


    def verify_button_labels(self):
        logger.info(f"Verifying all button labels on Browser Windows page")
        expect(self.new_tab_btn).to_have_text("New Tab")
        expect(self.new_window_btn).to_have_text("New Window")
        expect(self.new_message_window_btn).to_have_text("New Window Message")


    def click_new_tab_button(self):
        logger.info(f"Attempting to open new tab.")

        self.new_tab_btn.wait_for(state="visible")
        with self.page.expect_popup() as popup_info:
            self.new_tab_btn.click(force=True)

        new_tab = popup_info.value
        logger.info(f"New tab opened with URL: {new_tab.url}")
        new_tab.wait_for_load_state("domcontentloaded")
        return new_tab

    def click_btn_by_type(self, button_type: str):
        """Click Browser Windows button by type."""
        logger.info(f"Attempting to click button: {button_type}")

        button_map = {
            "new tab": self.new_tab_btn,
            "new window": self.new_window_btn,
            "new message window": self.new_message_window_btn,
        }

        if button_type not in button_map:
            raise Exception(f"Invalid button type provided: {button_type}."
                            f"Expected one of: {list(button_map.keys())}")

        button_map[button_type].wait_for(state="visible")
        with self.page.expect_popup() as popup_info:
            button_map[button_type].click(force=True)

        popup = popup_info.value

        if button_type in {"new tab", "new window"}:
            expect(popup).to_have_url(re.compile(f".*{popup.url}"))
            logger.info(f"New popup opened with URL: {popup.url}")
        else:
            logger.info(f"New Window Message opened")

        popup.wait_for_load_state("domcontentloaded")
        return popup

    def get_content_locator(self, popup: Page, button_type: str, text: str):
        logger.info(f"Retrieving locator for {button_type} to verify content {text}")
        if button_type == "new message window":
            return popup.locator("body")
        return popup.locator("#sampleHeading")














