from playwright.sync_api import Page, expect

from pages_demoqa.home.home_page import HomePage


class ElementsPage:

    def __init__(self, page: Page):
        self.page = page
        self._form_text_id = {}

    def enter_text_by_id(self, text_id, text):
        self.page.locator(f'#{text_id}').fill(text)
        self._form_text_id[text_id] = text

    def fill_text_boxes(self):
        home_pg = HomePage(self.page)
        home_pg.open()
        self.page.locator("h5:has-text('Elements')").click()
        self.page.locator("span:has-text('Text Box')").click()
        center_text = self.page.locator(".text-center")
        expect(center_text).to_have_text("Text Box")

        to_fill = {
            'userName': 'Noah BHYN',
            'userEmail': 'noah@yopmail.com',
            'currentAddress': '217 Commerce Dr, Exton PA 11291',
            'permanentAddress': '781 1st Ave, NY NY 19303'

        }

        for input_id, value in to_fill.items():
            self.enter_text_by_id(input_id, value)

        self.page.get_by_role('button', name='Submit').click()

    def verify_text_inputs(self):
        try:
            actual = (self.page.locator("#output").text_content() or "").lower()
            if not actual:
                print(f"[Failed] Missing {actual}")
                return False

            labels = {
                'userName': 'Name:',
                'userEmail': 'Email:',
                'currentAddress': 'Current Address :',
                'permanentAddress': 'Permananet Address :'
            }

            for field, value in self._form_text_id.items():
                expected = f"{labels.get(field, '')}{value}".lower()
                if expected not in actual:
                    print(f"[FAILED]Text field missing: {field}")
                    return False

            print("[PASSED] Text field verified successfully")
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

