import logging
import pytest
from playwright.sync_api import expect

from conftest import factory
from framework_playwright.playwright.pages.elements import ButtonsPage, RadioButtonPage
from framework_playwright.playwright.pages.elements.text_box_page import TextBoxPage


logger = logging.getLogger(__name__)

def test_text_box_input(page, base_url, factory):
    logger.info(f"--- Running Text Box Page Test ---")
    text_box = TextBoxPage(page, base_url)
    text_box.open()
    user_data = factory.get_text_box_data()
    text_box.fill_text_boxes(user_data)
    output_data = text_box.return_output_data()
    assert output_data == user_data



#--- Buttons ---

@pytest.mark.parametrize("button_type, expected_click",
                         [("doubleClick", "double click"),
                          ("rightClick", "right click"),
                          ("dynamicClick", "dynamic click"),])
def test_buttons_page(page, base_url, button_type, expected_click):
    logger.info(f"--- Running Buttons Page Test: {button_type} ---")
    buttons = ButtonsPage(page, base_url)
    buttons.open()
    buttons.click_button_by_loc(button_type)
    expected_msg = f"You have done a {expected_click}"
    expect(buttons.retrieve_clicked_message(button_type)).to_have_text(expected_msg)


#--- Radio Button ---

@pytest.mark.parametrize("radio_id, expected_status, expected_label",
                         [("yesRadio", "enabled", "Yes"),
                          ("impressiveRadio", "enabled", "Impressive"),
                          ("noRadio", "disabled", "No")]
                         )
def test_radio_button_page(page, base_url, radio_id, expected_status, expected_label):
    logger.info(f"--- Running Radio Button Test: {radio_id} - {expected_status} ---")
    radio_btn_page = RadioButtonPage(page, base_url)
    radio_btn_page.open()
    expect(radio_btn_page.question_text).to_have_text("Do you like the site?")
    expect(radio_btn_page.get_label_text_id(radio_id)).to_have_text(expected_label)

    if expected_status == "disabled":
        expect(radio_btn_page.get_radio_button_input(radio_id)).to_be_disabled()
    else:
        radio_btn_page.click_radio_button_by_content(radio_id)
        expected_msg = f"You have selected {radio_id.replace('Radio', '').capitalize()}"
        expect(radio_btn_page.success_message_loc).to_have_text(expected_msg)
