from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def type_text(self, selector: str, text: str):
        self.page.locator(selector).type(text)

    def press(self, selector: str, key: str):
        self.page.press(selector, key)

    def hover(self, selector: str):
        self.page.hover(selector)

    def drag_and_drop(self, source: str, target: str):
        self.page.drag_and_drop(source, target)

    def upload_file(self, selector: str, file_path: str):
        """Uploads a file to an input element (type='file')."""
        self.page.locator(selector).set_input_files(file_path)

    def get_text(self, selector: str):
        return self.page.locator(selector).inner_text()

    def get_all_text(self, selector: str):
        return self.page.locator(selector).all_inner_texts()

    def wait_visible(self, selector: str):
        self.page.locator(selector).wait_for(state="visible")

    def wait_text_contains(self, selector: str, text: str):
        expect(self.page.locator(selector)).to_contain_text(text)

    def take_screenshot(self, name: str = "screenshot.png"):
        self.page.screenshot(path=f"screenshots/{name}")


