import pytest
from playwright.sync_api import expect
import re

from framework_playwright.playwright.pages.home import HomePage

@pytest.mark.smoke
def test_navigation_to_alerts_section(page, base_url):
    home_page = HomePage(page)

    home_page.open()
    home_page.navigate_to_section("Alerts, Frame & Windows")
    home_page.select_menu_item("Alerts")

    expect(page).to_have_url(re.compile(rf"^{re.escape(base_url)}/alerts.*"))
    expect(page.locator(".text-center")).to_have_text("Alerts")


@pytest.mark.smoke
def test_navigation_to_frame_section(page, base_url):
    home_page = HomePage(page)

    home_page.open()
    home_page.navigate_to_section("Alerts, Frame & Windows")
    home_page.select_menu_item("Frames")

    expect(page).to_have_url(re.compile(rf"^{re.escape(base_url)}/frames.*"))
    expect(page.locator(".text-center")).to_have_text("Frames")