from playwright.sync_api import Playwright

from framework_playwright.playwright.pages.elements.elements_base import ElementsBase
from framework_playwright.playwright.pages.elements.text_box_page import TextBoxPage
from framework_playwright.playwright.pages.home import HomePage


def test_text_box_input(browser_instance):
    home = HomePage(browser_instance)
    text_box = TextBoxPage(browser_instance)
    elements_list = ElementsBase(browser_instance)

    home.open()
    home.handle_ad_popup()
    home.navigate_to_section("Elements")
    elements_list.select_menu_item("Text Box")

    user_data = {
        'userName': 'Noah BHYN',
        'userEmail': 'noah@yopmail.com',
        'currentAddress': '217 Commerce Dr, Exton PA 11291',
        'permanentAddress': '781 1st Ave, NY NY 19303'
    }


    text_box.fill_text_boxes(user_data)
    assert text_box.verify_output() is True

