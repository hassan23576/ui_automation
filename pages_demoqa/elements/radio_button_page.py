import re

from playwright.sync_api import expect

from pages_demoqa.elements.elements_base import ElementsBase


class RadioButtonPage(ElementsBase):
    def open(self):
        super().open()
        self.go_to("Radio Button")

    def verify_radio_buttons_selection(self):
        site_text = self.get_text('div.mb-3:has-text("Do you like the site?")')
        selected_text = self.page.locator("p:has-text('You have selected')")
        radio = [("yesRadio", "Yes"), ("impressiveRadio", "Impressive"), ("noRadio", "No")]

        for radio_id, expected in radio:
            input_el = self.page.locator(f"#{radio_id}")
            label_el = self.page.locator(f"label[for={radio_id}]")

            if input_el.is_disabled():
                print(f"Radio Button: {expected} is [Disabled]")
                continue

            label_el.click()
            selected_text.wait_for()
            assert "Do you like the site?" in site_text
            expect(selected_text).to_have_text(re.compile(fr"{expected}"))
            print(f"Successfully clicked radio button: {expected}")


