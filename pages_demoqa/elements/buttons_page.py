from playwright.sync_api import expect

from pages_demoqa.elements.elements_base import ElementsBase


class ButtonsPage(ElementsBase):

    def open(self):
        super().open()
        self.go_to("Buttons")

    def return_click_message(self, click_action):
        message = self.page.locator(f"#{click_action}ClickMessage")
        message.wait_for()
        return message.inner_text()

    def click_and_verify_buttons(self):
        expect(self.center_text).to_have_text("Buttons")
        buttons = [('Double Click Me', 'double'), ('Right Click Me', 'right'),
                   ('Click Me', 'dynamic')]

        for button_name, action_type in buttons:
            button_el = self.page.get_by_role("button", name=button_name, exact=True)
            button_el.scroll_into_view_if_needed()
            if action_type == 'double':
                button_el.dblclick()
            elif action_type == 'right':
                button_el.click(button='right')
            elif action_type == 'dynamic':
                button_el.click()

            message_el = self.page.locator(f"#{action_type}ClickMessage")
            message_el.wait_for()
            expect(message_el).to_have_text(f"You have done a {action_type} click")

            print(f"[{action_type}] click successful.")
