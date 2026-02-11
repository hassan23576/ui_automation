import logging
from selenium.webdriver.common.by import By

from framework_selenium.selenium.pages.base_page import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):

    EXPECTED_CARDS = [
        'Elements',
        'Forms',
        'Alerts, Frame & Windows',
        'Widgets',
        'Interactions',
        'Book Store Application'
    ]

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com"

    def open_home(self):
        self.open(self.url)
        assert self.url in self.driver.current_url

    def verify_banner(self):
        home_banner = (By.XPATH, '//img[@alt= "Selenium Online Training"]')
        return self.is_visible(home_banner)

    def verify_cards(self):
        card_names = self.get_all_texts((By.CSS_SELECTOR, '.card-body'))
        for name in card_names:
            title = name.split('\n')[0].strip()
            print("Verifying card: ", title)
            assert title in self.EXPECTED_CARDS, f"{title} not found in expected cards"

        logger.info("All card names verified successfully.")
        return True



