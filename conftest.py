import allure
import pytest

# def pytest_addoption(parser):
#     parser.addoption("--browser_name", action="store", default="chrome")
#     parser.addoption("--base_url", action="store", default="https://demoqa.com")
#
#
# @pytest.fixture(scope="session")
# def base_url(request):
#     return request.config.getoption("--base_url")
#
#
# @pytest.fixture
# def page(playwright, request, base_url):
#     # Select browser type
#     browser_name = request.config.getoption("--browser_name")
#     browser_type = playwright.chromium if browser_name == "chrome" else playwright.firefox
#
#     # Launch browser
#     browser = browser_type.launch(headless=False)
#
#     context = browser.new_context(base_url=base_url, viewport={'width': 1920, 'height': 1080})
#
#     new_page = context.new_page()
#     yield new_page
#
#     context.close()
#     browser.close()



@pytest.fixture
def browser_context_args(browser_context_args, base_url):
    """
    Overrides the default context arguments.
    'base_url' here is the built-in Playwright fixture.
    """
    return {
        **browser_context_args,
        "viewport": {'width': 1920, 'height': 1080},
        "base_url": base_url
    }



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Runs after each test phase.
    We attach Allure artifacts ONLY if the test failed during the 'call' phase.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("browser_instance", None)
        if not page:
            return

        # Screenshot
        try:
            allure.attach(
                page.screenshot(full_page=True),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass

        # Page URL
        try:
            allure.attach(
                page.url or "No URL available",
                name="Page URL",
                attachment_type=allure.attachment_type.TEXT,
            )
        except Exception:
            pass

        # Console logs (if captured)
        try:
            console_messages = getattr(page, "_console_messages", [])
            if console_messages:
                allure.attach(
                    "\n".join(console_messages),
                    name="Browser Console Logs",
                    attachment_type=allure.attachment_type.TEXT,
                )
        except Exception:
            pass




