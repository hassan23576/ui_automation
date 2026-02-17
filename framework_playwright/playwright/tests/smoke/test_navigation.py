import logging
import pytest
from playwright.sync_api import expect
import re

from framework_playwright.playwright.pages.home import HomePage
from framework_playwright.playwright.pages.sidebar import Sidebar

logger = logging.getLogger(__name__)

@pytest.mark.smoke
def test_navigation_to_alerts_section(page, base_url):
    home_page = HomePage(page, base_url)

    home_page.open()
    home_page.navigate_to_section("Alerts, Frame & Windows")
    home_page.select_menu_item("Alerts")

    expect(page).to_have_url(re.compile(rf"^{re.escape(base_url)}/alerts.*"))
    expect(page.locator(".text-center")).to_have_text("Alerts")


@pytest.mark.smoke
def test_navigation_to_frame_section(page, base_url):
    home_page = HomePage(page, base_url)

    home_page.open()
    home_page.navigate_to_section("Alerts, Frame & Windows")
    home_page.select_menu_item("Frames")

    expect(page).to_have_url(re.compile(rf"^{re.escape(base_url)}/frames.*"))
    expect(page.locator(".text-center")).to_have_text("Frames")


@pytest.mark.smoke
@pytest.mark.parametrize("elements_group, menu_list_item",
                         [("Elements", "Text Box"),
                          # ("Elements", "Check Box"),
                          # ("Elements", "Radio Button"),
                          # ("Elements", "Web Tables"),
                          # ("Elements", "Buttons"),
                          # ("Elements", "Links"),
                          # ("Elements", "Broken Links - Images"),
                          # ("Elements", "Upload and Download"),
                          # ("Elements", "Dynamic Properties")
                          ])
def test_elements_menu_list_navigation(page, base_url, elements_group, menu_list_item):
    logger.info(f"--- Running Elements Menu List Navigation ---")
    home_page = HomePage(page, base_url)
    side_bar_page = Sidebar(page, base_url)

    home_page.open()
    home_page.navigate_to_section("Elements")
    title = side_bar_page.select_side_bar_option(elements_group, menu_list_item)
    assert title.strip() == menu_list_item.strip(), (
        f"Navigation Mismatch! Clicked on '{menu_list_item}'"
        f"but the page header showed '{title}'"
    )
    logger.info(f"Navigation Successful to: '{menu_list_item}'!")