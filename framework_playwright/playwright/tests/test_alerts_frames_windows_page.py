import logging
import re

import pytest
from playwright.sync_api import expect, Page


from framework_playwright.playwright.pages.alert_windows.alerts_page import AlertPage
from framework_playwright.playwright.pages.alert_windows.browser_windows_page import BrowserWindowsPage
from framework_playwright.playwright.pages.alert_windows.frames_page import FramesPage
from framework_playwright.playwright.pages.alert_windows.nested_frames_page import NestedFramesPage

logger = logging.getLogger(__name__)

#--- TEST ALERTS PAGE---

@pytest.mark.parametrize("button_type, expected_message, prompt_text, action",
                         [
                             ("simple", "You clicked a button", None, "accept"),
                             ("timer", "This alert appeared after 5 seconds", None, "accept"),
                             ("confirm", "Do you confirm action?", None, "accept"),
                             ("confirm", "Do you confirm action?", None, "dismiss"),
                             ("prompt", "Please enter your name", "Noah", "accept"),
                             ("prompt", "Please enter your name", "Noah", "dismiss")

                         ])

def test_alerts_page(page, base_url, button_type, expected_message, prompt_text, action):
    """Run these multiple times for functional logic"""
    alerts_page = AlertPage(page, base_url)
    alerts_page.open()

    def handle_dialog(dialog):
        assert dialog.message == expected_message
        if action == "dismiss":
            dialog.dismiss()
        else:
            dialog.accept(prompt_text=prompt_text) if prompt_text else dialog.accept()

    page.once("dialog", handle_dialog)
    alerts_page.click_button_by_type(button_type)

    if button_type == "confirm":
        expected_text = "You selected Ok" if action == "accept" else "You selected Cancel"
        expect(alerts_page.confirm_result).to_have_text(expected_text)

    elif button_type == "prompt":
        if action == "accept":
            expect(alerts_page.prompt_result).to_have_text(f"You entered {prompt_text}")
        else:
            expect(alerts_page.prompt_result).not_to_be_visible()



def test_alerts_ui_health(page, base_url):
    """Run this to ensure the UI labels are displayed correctly."""
    alerts_page = AlertPage(page, base_url)
    alerts_page.open()
    alerts_page.verify_instruction_labels()
    alerts_page.verify_all_button_texts()


#--- TEST FRAMES PAGE ---

def test_frames_page_simple_frame_text(page, base_url):
    """Verify the frames page is displayed correctly."""
    frames_page = FramesPage(page, base_url)
    frames_page.open()

    frame_data = [
        (frames_page.frame_one, "Parent Frame"),
        (frames_page.frame_two, "Child Frame")
    ]

    for locator, name in frame_data:
        logger.debug(f"Attempting to verify: {name}")

        expect(locator).to_have_text("This is a sample page")
        logger.info(f"Success: {name} contains 'This is a sample page'")


#--- TEST NESTED FRAMES PAGE ---

def test_nested_frames_page_child_and_parent(page, base_url):
    """Verify the nested frames page is displayed correctly."""
    frames_page = NestedFramesPage(page, base_url)
    frames_page.open()

    frame_expectation = {
        frames_page.parent_frame: "Parent frame",
        frames_page.child_frame: "Child Iframe",

    }
    for locators, expected_text in frame_expectation.items():
        logger.debug(f"Verifying locators: {locators} expected_text: '{expected_text}'")

        expect(locators).to_have_text(expected_text)
        logger.info(f"Successfully verified text: '{expected_text}'")



def test_new_tab_opens_and_sample_heading(page, base_url):
    """Verify the new tab opens and sample heading is displayed correctly."""
    browser_page = BrowserWindowsPage(page, base_url)
    browser_page.open()

    new_tab = browser_page.click_new_tab_button()

    logger.info(f"Verifying new tab URL and content")
    expect(new_tab).to_have_url(re.compile(f".*/sample"))
    expect(new_tab.get_by_text("This is a sample page")).to_be_visible()

    new_tab.close()
    logger.info(f"New tab verified and closed.")



@pytest.mark.parametrize("button_type, expected_message",
                         [("new tab", "This is a sample page"),
                          ("new window", "This is a sample page"),
                          ("new message window", "Knowledge increases by sharing"),])
def test_new_browser_windows_open_and_content(page, base_url, button_type, expected_message):
    """Verify Browser Windows opens and inner content is displayed correctly."""

    browser_page = BrowserWindowsPage(page, base_url)
    browser_page.open()

    popup = browser_page.click_btn_by_type(button_type)

    logger.info(f"Verifying popup window content: {expected_message}")

    try:
        target = browser_page.get_content_locator(popup, button_type, expected_message)
        browser_page.verify_text(target, expected_message)
    finally:
        popup.close()























