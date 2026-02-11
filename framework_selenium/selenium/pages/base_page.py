
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_all_texts(self, locator) -> list[str]:
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return [el.text for el in elements]

    def get_attribute(self, locator, attribute: str) -> str:
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    def exists(self, locator) -> bool:
        try:
            self.driver.find_element(*locator)
            return True
        except Exception:
            return False

    def get_count(self, locator) -> int:
        elements = self.driver.find_elements(*locator)
        return len(elements)