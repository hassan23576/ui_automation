
import logging
import os
import random
import re
from datetime import datetime
from pathlib import Path

from playwright.sync_api import expect

from framework_playwright.playwright.pages.base_page import BasePage

IMAGES_FOLDER = "assets"
logger = logging.getLogger(__name__)


class PracticeFormPage(BasePage):
    path = "/automation-practice-form"

    def __init__(self, page, base_url):
        super().__init__(page, base_url)

    @property
    def student_reg_form_loc(self):
        """Returns the locator of the student registration form title"""
        return self.page.locator("h5")

    @property
    def get_form_labels(self):
        """Returns list of form labels"""
        return self.page.locator("form #userForm").locator("label").all_inner_texts()

    @property
    def get_date_of_birth_loc(self):
        return self.page.locator("#dateOfBirthInput")


    def open(self):
        super().open_page(self.path, "Practice Form")


    def fill_form(self, data):
        logger.info(f"Filling {data.items()} in form..")
        root_dir = Path(__file__).resolve().parents[3]
        file_path = root_dir / "assets" / "test_image.png"

        text_fields = ["First Name", "Last Name", "name@example.com", "Mobile Number", "Current Address"]

        for key, value in data.items():
            if key in text_fields:
                self.page.get_by_placeholder(key).fill(value)


        self.page.locator("#subjectsContainer").get_by_role("combobox").fill("English")
        self.page.keyboard.press("Enter")
        gender = self.select_random_item("[for^='gender-radio']")
        date_of_birth = self.return_random_selected_dob()
        hobbies = self.select_random_item("label[for^='hobbies-checkbox']")

        input_field = self.page.locator("#uploadPicture")
        input_field.scroll_into_view_if_needed()
        input_field.set_input_files(str(file_path))
        picture_name = file_path.name
        state = self.select_random_from_dropdown("#state", "[role='option']")
        city = self.select_random_from_dropdown("#city", "[role='option']")
        self.page.locator("#submit").click()
        return {
            "Student Name": f"{data.get('First Name')} {data.get('Last Name')}",
            "Student Email": data["name@example.com"],
            "Gender": gender,
            "Date of Birth": date_of_birth,
            "Subjects": "English",
            "Hobbies": hobbies,
            "Picture": picture_name,
            "Address": data["Current Address"],
            "State and City": f"{state} {city}"
        }



    def return_random_selected_dob(self):
        logger.info("Selecting random Date of Birth..")
        self.get_date_of_birth_loc.click()
        days = self.page.locator("[role='gridcell'][aria-disabled='false']")
        cell = days.nth(random.randint(0, days.count() -1))
        label = cell.get_attribute("aria-label").split(", ", 1)
        full_date = label[1].strip().replace(",", "")
        cell.click()
        logger.info(f"Selected date of birth: {full_date}")
        expect(days).not_to_be_visible()
        input_value = self.get_date_of_birth_loc.input_value()

        new_label = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', full_date)
        logger.info(f"new_label:{new_label}")
        date_obj = datetime.strptime(new_label, "%B %d %Y")
        formatted_date = date_obj.strftime("%d %b %Y")

        assert input_value == formatted_date
        return input_value


    def get_confirmation_modal_data(self):

        modal_table = self.page.locator(".modal-content table")
        modal_table.wait_for(state="visible")

        actual_data = {}
        rows = modal_table.locator("tbody tr").all()

        for row in rows:
            cells = row.locator("td").all()
            if len(cells) == 2:
                label = cells[0].inner_text().strip()
                value = cells[1].inner_text().strip()
                actual_data[label] = value
        return actual_data





































