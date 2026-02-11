import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--selenium-browser", action="store", default="chrome", help="Browser: chrome")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("selenium_browser").lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()



