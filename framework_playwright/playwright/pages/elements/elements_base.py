from playwright.sync_api import Page, expect

from framework_playwright.playwright.pages.base_page import BasePage


class ElementsBase(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.element_group = self.page.locator("div.element-group:has(.header-text:has-text('Elements'))").first
        self.header = self.page.locator(".header-text")
        self.menu_items = self.element_group.locator(".menu-list li span.text")
        self.center_text = self.page.locator(".text-center")

    def open(self):
        """Go to the main Elements Page."""
        self.goto("https://demoqa.com/elements")
        # expect(self.header).to_be_visible()

    def go_to(self, item_text: str):
        """Click a menu item on the left panel by visible text."""
        is_open = self.element_group.locator(".element-list.collapse.show").count() > 0
        if not is_open:
            self.header.click()
            expect(self.element_group.locator(".element-list.collapse.show")).to_be_visible()

        target = self.menu_items.filter(has_text=item_text).first
        expect(target).to_be_visible()
        target.click()


    def select_menu_item(self, item_name: str):
        menu_list = self.page.locator(".left-pannel .menu-list span", has_text=item_name)
        menu_list.wait_for(state="visible")
        menu_list.click()

