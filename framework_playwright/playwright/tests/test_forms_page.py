import logging
import re

from playwright.sync_api import expect

from framework_playwright.playwright.pages.forms.practice_form_page import PracticeFormPage
from framework_playwright.playwright.pages.home import HomePage
from framework_playwright.playwright.pages.sidebar import Sidebar

logger=logging.getLogger(__name__)


def test_practice_form(page, base_url, factory):
    logger.info(f"--- Running Elements Menu List Navigation ---")
    home_page = HomePage(page, base_url)
    side_bar_page = Sidebar(page, base_url)
    practice_form = PracticeFormPage(page, base_url)

    home_page.open()
    home_page.navigate_to_section("Elements")
    side_bar_page.select_side_bar_option("Forms", "Practice Form")

    student_reg_title = practice_form.student_reg_form_loc
    expect(student_reg_title).to_have_text(re.compile("^Student Registration Form$"))


    user_data = {'First Name': factory.first_name(), 'Last Name': factory.last_name(), 'name@example.com': factory.email(),
                 'Mobile Number': factory.mobile_number(), 'Current Address': factory.address(),
                 }
    expected = practice_form.fill_form(user_data)

    actual = practice_form.get_confirmation_modal_data()
    assert actual == expected