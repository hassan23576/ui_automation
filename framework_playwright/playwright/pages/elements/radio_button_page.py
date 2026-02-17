import re

import logging
from playwright.sync_api import expect

from framework_playwright.playwright.pages.base_page import BasePage

logger=logging.getLogger(__name__)


class RadioButtonPage(BasePage):
    path = "/radio-button"


    def __init__(self, page, base_url):
        super().__init__(page, base_url)

    @property
    def question_text(self):
        return self.page.locator("div.mb-3")

    @property
    def success_message_loc(self):
        return self.page.locator(".mt-3")

    def get_radio_button_input(self, button_type: str):
        return self.page.locator(f"#{button_type}")

    def get_label_text_id(self, radio_id):
        """Return the text of the radio button"""
        return self.page.locator(f"#{radio_id} + label")

    def open(self):
        super().open_page(self.path, "Radio Button")

    def click_radio_button_by_content(self, button_type: str):
        """
        Click radio button based on parameterized content type
        """
        radio_label = self.page.locator(f"label[for={button_type}]")

        if not radio_label.is_visible(timeout=5000):
            error_msg = f"Radio Label '{button_type}' not visible."
            raise RuntimeError(error_msg)

        logger.info(f"Clicking Radio Button: {button_type}")
        return radio_label.click()


    def verify_radio_buttons_selection(self):
        site_text = self.get_text('div.mb-3:has-text("Do you like the site?")')
        selected_text = self.page.locator("p:has-text('You have selected')")
        radio = [("yesRadio", "Yes"), ("impressiveRadio", "Impressive"), ("noRadio", "No")]

        for radio_id, expected in radio:
            input_el = self.page.locator(f"#{radio_id}")
            label_el = self.page.locator(f"label[for={radio_id}]")

            if input_el.is_disabled():
                print(f"Radio Button: {expected} is [Disabled]")
                continue

            label_el.click()
            selected_text.wait_for()
            assert "Do you like the site?" in site_text
            expect(selected_text).to_have_text(re.compile(fr"{expected}"))
            print(f"Successfully clicked radio button: {expected}")


