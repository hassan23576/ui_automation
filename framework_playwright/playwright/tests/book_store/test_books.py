import logging
from time import sleep

from playwright.sync_api import expect

from framework_playwright.playwright.pages.login_page import LoginPage

logger = logging.getLogger(__name__)

def test_user_can_see_added_books(api_user, bookstore_api, page, base_url):
    user_id = api_user['userId']
    username = api_user['username']
    password = api_user['password']

    token = bookstore_api.generate_token(username, password)
    isbns = ['9781449325862']

    try:
        add_books_response = bookstore_api.add_books(user_id, token, isbns)
        logger.info(f"Books added response: {add_books_response}")

        login_page = LoginPage(page, base_url)
        login_page.open_login_page()
        login_page.perform_login(username, password)

        expect(page.locator("text=Git Pocket Guide")).to_be_visible()

    finally:
        fresh_token = bookstore_api.generate_token(username, password)
        bookstore_api.delete_all_books(user_id, fresh_token)







