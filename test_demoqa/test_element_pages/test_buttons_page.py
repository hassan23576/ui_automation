from pages_demoqa.elements.buttons_page import ButtonsPage


def test_buttons_page(browser_instance):
    buttons = ButtonsPage(browser_instance)
    buttons.open()
    buttons.click_and_verify_buttons()