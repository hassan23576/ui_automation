import logging
from playwright.sync_api import expect

logger = logging.getLogger(__name__)


def test_login_success_and_profile_visibility(auth_page):
    expect(auth_page.logout_button).to_be_visible()



def test_create_user_and_generate_token(api_auth_state):
    auth= api_auth_state

    logger.info(f"Auth path is {auth}")