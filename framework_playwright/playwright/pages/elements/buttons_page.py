import logging

from framework_playwright.playwright.pages.base_page import BasePage

logger = logging.getLogger(__name__)

class ButtonsPage(BasePage):
    path = "/buttons"

    def __init__(self, page, base_url):
        super().__init__(page, base_url)

    @property
    def double_click_loc(self):
        """Return the Double Click Locator"""
        return self.page.locator("#doubleClickBtn")

    @property
    def right_click_loc(self):
        """Return the Right Click Locator"""
        return self.page.locator("#rightClickBtn")

    @property
    def dynamic_click_loc(self):
        """Return the dynamic Click Locator"""
        return self.page.get_by_role("button", name="Click Me", exact=True)

    def retrieve_clicked_message(self, button_type):
        """Return the clicked message"""
        msg_loc = self.page.locator(f"#{button_type}Message")
        return msg_loc

    def open(self):
        super().open_page(self.path, "Buttons")

    def click_button_by_loc(self, button_type):
        """Click Button based on parametrized button type"""
        mapping = {
            "doubleClick": lambda: self.double_click_loc.dblclick(),
            "rightClick": lambda: self.right_click_loc.click(button="right"),
            "dynamicClick": lambda: self.dynamic_click_loc.click()

        }

        if button_type not in mapping:
            raise Exception(f"Invalid button type {button_type}")
        logger.info(f"Clicking '{button_type}' button")

        mapping[button_type]()







