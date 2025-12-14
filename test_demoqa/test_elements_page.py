from playwright.sync_api import Playwright

from pages_demoqa.elements.elements_page import ElementsPage


def test_text_box_input(playwright: Playwright, browser_instance):
    elements_page = ElementsPage(browser_instance)
    elements_page.fill_text_boxes()
    elements_page.verify_text_inputs()

