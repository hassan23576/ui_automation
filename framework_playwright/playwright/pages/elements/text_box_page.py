import logging
from playwright.sync_api import Page
from faker import Faker

from framework_playwright.playwright.pages.base_page import BasePage

logger = logging.getLogger(__name__)

class TextBoxPage(BasePage):
    path = "/text-box"


    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.page = page

    @property
    def submit_btn_loc(self):
        """Return Submit Button Locator"""
        return self.page.get_by_role("button", name="Submit", exact=True)

    def get_element(self, loc):
        return self.page.locator(f"#{loc}")

    def open(self):
        super().open_page(self.path, "Text Box")

    def fill_text_boxes(self, user_data: dict):
       """Fills text boxes with placeholder text."""
       mapping = {
           "userName": user_data["full_name"],
           "userEmail": user_data["email"],
           "currentAddress": user_data["address"],
           "permanentAddress": user_data["permanent_address"],
       }
       logger.info(f"Attempting to fill text box with user data: {user_data}")
       for field, value in mapping.items():
           if value:
            logger.debug(f"Filling field: '{field}' value: '{value}'")
            self.get_element(field).fill(value)

       logger.info(f"Form filling complete, submitting..")
       self.submit_btn_loc.click()


    def return_output_data(self):
        """Verifying output data."""
        output_text = {}

        output_container = self.get_element("output")
        try:
            output_container.wait_for(timeout=5000)
        except Exception:
            raise Exception("Result output box didn't appear after clicking Submit button")

        mapping = {
            "name":  ["Name", "full_name"],
            "email": ["Email", "email"],
            "currentAddress": ["Current Address", "address"],
            "permanentAddress": ["Permananet Address", "permanent_address"]
        }
        for field,(expected_label, label_info) in mapping.items():
            line_text = output_container.locator(f"#{field}").inner_text()
            result = line_text.split(":", 1)
            actual_label = result[0].strip()
            actual_value = result[1].strip()
            output_text[label_info] = actual_value
            assert actual_label == expected_label, \
                f"Label Mismatch! UI showed '{actual_label}' but expected '{expected_label}' at ID: {field}"
        logger.info(f"Successfully retrieved output data: {output_text}")
        return output_text











