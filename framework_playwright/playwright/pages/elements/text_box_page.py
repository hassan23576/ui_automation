import logging
from playwright.sync_api import Page

from framework_playwright.playwright.pages.base_page import BasePage


class TextBoxPage(BasePage):
    logger = logging.getLogger(__name__)

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.page = page
        self.path = "/textbox"
        self._form_data = {}

    def fill_text_boxes(self, data: dict):
        self.verify_text(self.page.locator(".text-center"), "Text Box")

        for input_id, value in data.items():
            locator = self.page.locator(f"#{input_id}")
            self.enter_text(locator, value)
            self._form_data[input_id] = value

        self.page.get_by_role('button', name='Submit').click()

    def verify_output(self):
        try:
            actual = (self.page.locator("#output").inner_text() or "").lower()
            if not actual:
                self.logger.error(f"[Failed] Missing {actual}")
                return False

            labels = {
                'userName': 'Name:',
                'userEmail': 'Email:',
                'currentAddress': 'Current Address :',
                'permanentAddress': 'Permananet Address :' # Note: DemoQA has a typo 'Permananet'
            }

            for field, value in self._form_data.items():
                expected_label = labels.get(field, "")
                expected_string = f"{expected_label}{value}".lower()

                if expected_string not in actual:
                    print(f"[FAILED]Expected: {expected_string}' not found in output")
                    return False

            self.logger.info("[PASSED] All Text fields verified in output successfully")
            return True
        except Exception as e:
            self.logger.exception(f"Error during verification{e}")
            return False

