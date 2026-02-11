import re


import logging
from playwright.sync_api import Page, expect

from framework_playwright.playwright.pages.base_page import BasePage


logger = logging.getLogger(__name__)

class AlertPage(BasePage):
    path = "/alerts"


    def __init__(self, page: Page, base_url: str):
       super().__init__(page, base_url)

    #--- TRIGGER BUTTONS
    @property
    def simple_btn(self):
        return self.page.locator("#alertButton")

    @property
    def timer_alert_btn(self):
        return self.page.locator("#timerAlertButton")

    @property
    def confirm_btn(self):
        return self.page.locator("#confirmButton")

    @property
    def prompt_btn(self):
        return self.page.locator("#promtButton")

    #--- INSTRUCTION LABELS --
    @property
    def simple_label(self):
        return self.page.locator("#javascriptAlertsWrapper div.row").filter(has=self.simple_btn).locator("span")

    @property
    def timer_alert_label(self):
        return self.page.locator("#javascriptAlertsWrapper div.row").filter(has=self.timer_alert_btn).locator("span")

    @property
    def confirm_label(self):
        return self.page.locator("#javascriptAlertsWrapper div.row").filter(has=self.confirm_btn).locator("span")

    @property
    def prompt_label(self):
        return self.page.locator("#javascriptAlertsWrapper div.row").filter(has=self.prompt_btn).locator("span")

    #--- RESULT LABELS ---
    @property
    def confirm_result(self):
        return self.page.locator("#confirmResult")

    @property
    def prompt_result(self):
        return self.page.locator("#promptResult")


    def open(self):
        logger.info(f"Opening Alerts page: {self.base_url}{self.path}")
        self.navigate_to(self.path)
        expect(self.page).to_have_url(re.compile(f".*{self.path}$"))
        self.verify_text(self.page.locator(".text-center"), "Alerts")


    def verify_instruction_labels(self):
        logger.info("Verifying all instruction labels on Alerts page")
        expect(self.simple_label).to_have_text("Click Button to see alert")
        expect(self.timer_alert_label).to_have_text("On button click, alert will appear after 5 seconds")
        expect(self.confirm_label).to_have_text("On button click, confirm box will appear")
        expect(self.prompt_label).to_have_text("On button click, prompt box will appear")

    def verify_all_button_texts(self):
        logger.info("Verifying all buttons display 'Click me'")
        buttons = [self.simple_btn, self.timer_alert_btn, self.confirm_btn, self.prompt_btn]
        for btn in buttons:
            expect(btn).to_have_text("Click me")


    def click_button_by_type(self, button_type: str):
        """
        Click alert button based on parametrized input type
        """
        button_map = {
            "simple": self.simple_btn,
            "timer": self.timer_alert_btn,
            "confirm": self.confirm_btn,
            "prompt": self.prompt_btn
        }

        if button_type not in button_map:
            raise Exception(f"Invalid button type provided: {button_type}."
                            f"Expected one of: {list(button_map.keys())}")

        logger.info(f"Triggering {button_type} alert")
        button_map[button_type].click()










