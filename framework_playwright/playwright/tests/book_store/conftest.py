import pytest

from framework_playwright.playwright.pages.login_page import LoginPage
from utils.api_utils import create_dynamic_user, generate_token, save_api_auth_state


@pytest.fixture(scope="session")
def api_user():
    """Create a user via API and provides credentials in the suite"""

    user_data = create_dynamic_user()
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
def api_auth_state():
    """Bypasses UI login by creating a user and token via API."""
    # Create User
    user = create_dynamic_user()
    # Get Token
    token = generate_token(user["username"], user["password"])
    # Save JSON
    auth_data = {"token": token, "username": user["username"]}
    auth_path = save_api_auth_state(auth_data)

    return auth_path