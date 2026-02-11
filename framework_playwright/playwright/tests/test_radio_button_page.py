from framework_playwright .playwright.pages.elements.radio_button_page import RadioButtonPage

def test_radio_button(browser_instance):
    radio_button = RadioButtonPage(browser_instance)
    radio_button.open()
    radio_button.verify_radio_buttons_selection()
