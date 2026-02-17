import logging

from framework_playwright.playwright.pages.base_page import BasePage


logger = logging.getLogger(__name__)


class PracticeFormPage(BasePage):
    path = "/automation-practice-form"

    def __init__(self, page, base_url):
        super().__init__(page, base_url)

    @property
    def student_reg_form_loc(self):
        return self.page.locator("h5")

    def open(self):
        super().open_page(self.path, "Practice Form")

