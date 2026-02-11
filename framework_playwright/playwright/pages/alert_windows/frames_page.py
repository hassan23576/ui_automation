import logging
import re

from playwright.sync_api import expect

from framework_playwright.playwright.pages.base_page import BasePage


logger = logging.getLogger(__name__)


class FramesPage(BasePage):
    path = "/frames"

    def __init__(self, page, base_url):
        super().__init__(page, base_url)

    #--- IFRAMES ---
    @property
    def frame_one(self):
        return self.page.frame_locator("#frame1").locator("#sampleHeading")

    @property
    def frame_two(self):
        return self.page.frame_locator("#frame2").locator("#sampleHeading")

    def open(self):
        logger.info(f"Opening Frames page: {self.base_url}{self.path}")
        self.navigate_to(self.path)
        expect(self.page).to_have_url(re.compile(f".*{self.path}$"))
        self.verify_text(self.page.locator(".text-center"), "Frames")
