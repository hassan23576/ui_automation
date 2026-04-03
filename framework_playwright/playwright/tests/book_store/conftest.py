import pytest
from playwright.sync_api import Browser
from framework_playwright.playwright.api.bookstore_api import BookStoreApi
from framework_playwright.playwright.pages.login_page import LoginPage


@pytest.fixture(scope="session")
def bookstore_api():
    return BookStoreApi()

@pytest.fixture(scope="session")
def api_user(bookstore_api):
    """Create a user via API and provides credentials in the suite"""

    user_data = bookstore_api.create_dynamic_user()
    return user_data



@pytest.fixture
def auth_page(page, api_user, base_url):
    login_page = LoginPage(page, base_url)
    login_page.open_login_page()
    login_page.perform_login(
        user=api_user["username"],
        pwd=api_user["password"]
    )
    yield login_page


@pytest.fixture(scope="session")
def api_auth_state(bookstore_api, api_user):
    """Bypasses UI login by creating a user and token via API."""
    token = bookstore_api.generate_token(
        api_user["username"],
        api_user["password"]
    )

    auth_data = {
        "token": token,
        "username": api_user["username"],
        "userId": api_user["userId"]
    }

    auth_path = bookstore_api.save_api_auth_state(auth_data)
    return auth_path

@pytest.fixture
def authenticated_page(browser: Browser, api_auth_state, base_url):
    """Creates a browser page with pre-authenticated state"""
    context = browser.new_context(
        storage_state=api_auth_state,
        base_url=base_url
    )
    page = context.new_page()
    yield page
    context.close()