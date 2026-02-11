import logging
import re

from playwright.sync_api import Page, expect

from framework_playwright.playwright.pages.base_page import BasePage

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    path = "/login"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @property
    def username_field(self):
        return self.page.get_by_placeholder("UserName")

    @property
    def password_field(self):
        return self.page.get_by_placeholder("Password")

    @property
    def login_button(self):
        return self.page.locator("#login")

    @property
    def logout_button(self):
        return self.page.get_by_role("button", name="Log out")

    def open_login_page(self):
        logger.info(f"Opening login page: {self.base_url}{self.path}")
        self.navigate_to(self.path)
        expect(self.page).to_have_url(re.compile(f".*{self.path}$"))
        self.verify_text(self.page.locator(".text-center"), "Login")

    def perform_login(self, user, pwd):
        try:
            logger.info(f"Performing login: {user}")
            self.username_field.fill(user)
            self.password_field.fill(pwd)
            self.login_button.click()

            expect(self.page).to_have_url(re.compile(f".*/profile"), timeout=10000)

            expect(self.logout_button).to_be_visible(timeout=5000)
            logger.info(f"Logged successful: {user}")

        except Exception as e:
            logger.error(f"Login failed for: {user}. Current URL: {self.page.url}")
            logger.debug(f"Error Details: {str(e)}")
            raise




