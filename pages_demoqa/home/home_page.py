from playwright.sync_api import Page, expect


class HomePage:

    EXPECTED_CARDS = [
        'Elements',
        'Forms',
        'Alerts, Frame & Windows',
        'Widgets',
        'Interactions',
        'Book Store Application'
    ]

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://demoqa.com/"

    def open(self):
        self.page.goto(self.url)
        expect(self.page).to_have_url(self.url)
        header_img = self.page.locator('//img[@src="/images/Toolsqa.jpg"]')
        expect(header_img).to_be_visible()

    def verify_banner_visible(self):
        try:
            home_banner = self.page.locator("img[alt= 'Selenium Online Training']")
            expect(home_banner).to_be_visible()
            print("\nHome banner is visible.")
            return True

        except Exception as e:
            print(f"[FAIL] Home banner not visible {e}")
            return False

    def verify_cards(self, expected_cards: list[str] | None = None) -> bool:
        try:
            expected_cards = expected_cards or self.EXPECTED_CARDS

            card_names = self.page.locator(".card-body").all_inner_texts()
            for name in card_names:
                print(f"Verifying card: {name}")
                assert name in expected_cards, f"{name} not found in expected cards"
                return True

            print("All card names verified successfully.")
        except Exception as e:
            print(f"Verification failed: {e}")
