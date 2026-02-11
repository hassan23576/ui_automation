import pytest

from framework_selenium.selenium.pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.selenium
def test_homepage(driver):
    homepage = HomePage(driver)
    homepage.open_home()
    homepage.verify_banner()
    homepage.verify_cards()
