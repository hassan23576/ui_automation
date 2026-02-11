import json
import logging
import os
import uuid
from pathlib import Path

import requests
from dotenv import load_dotenv


# Project Root at the top using Pathlib
# This goes: utils/api_utils.py -> utils -> Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")

with open(PROJECT_ROOT / "data" / "config.json") as f:
    config = json.load(f)

BASE_URL = config["base_url"]
ENDPOINTS = config["endpoints"]

logger = logging.getLogger(__name__)



def create_dynamic_user():
    """Generate a unique user using API and return user credentials"""
    username = f"user_{uuid.uuid4().hex[:8]}"
    #Fetch password from the environment variable
    password = os.getenv("DEMOQA_PASSWORD")

    if not password:
        raise Exception("DEMOQA_PASSWORD not found in environment variables!")

    # Use endpoint
    url = f"{BASE_URL}{ENDPOINTS['create_user']}"
    payload = {"userName": username, "password": password}

    logger.info(f"Attempting to create dynamic user: {username}")

    response = requests.post(url, json=payload)

    if response.status_code == 201:
        api_data = response.json()

        #--- DATA VALIDATION ---
        actual_name = api_data.get("username")
        user_id = api_data.get("userID")

        # Verify the username matches what we sent
        if actual_name != username:
            logger.error(f"DATA MISMATCH: Sent '{username}' but API returned '{actual_name}' ")
            raise ValueError("Username mismatch in API response.")

        # Verify a UserID was generated
        if not user_id:
            logger.error(f"API Error: Response was: {response.status_code} and 'UserID' is missing.")
            raise ValueError("No userID returned from API response.")


        logger.info(f"Successfully created user: {user_id}")
        # Return a dictionary
        return {
            "userId": user_id,
            "username": username,
            "password": password
        }
    else:
        logger.error(f"User creation failed! Status: {response.status_code} Body: {response.text} ")
        raise Exception(f"Failed creating user: {response.status_code}")



def generate_token(username, password):
    """Generate a token for user"""
    url = f"{BASE_URL}{ENDPOINTS['generate_token']}"
    payload = {"userName": username, "password": password}

    logger.info(f"Attempting to generate token for dynamic user: {username}")
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        api_data = response.json()
        token = api_data.get("token")
        status = api_data.get("status")

        if token:
            masked_token = f"{token[:10]}....."
            logger.info(f"New token received: {masked_token}")

        if status == "Success":
            logger.info(f"Successfully generated user token for status: {status}")
            return token

        logger.warning(f"Token request returned status {status}")
        return None
    else:
        logger.error(f"Failed to generate user token! Status: {response.status_code}")
        raise Exception("Failed to generate user token!")


def save_api_auth_state(auth_data):
    """Take API login response and builds the Playwright JSON file using absolute paths"""

    # Construct path for the .auth directory
    auth_dir = PROJECT_ROOT / "framework_playwright" / "playwright" / ".auth"

    logger.info(f"Preparing to save auth state to: {auth_dir}")

    state = {
        "cookies": [
            {
                "name": "token",
                "value": auth_data["token"],
                "domain": "demoqa.com",
                "path": "/",
                "expires": -1,
                "httpOnly": False,
                "secure": False,
                "sameSite": "None",
            }
        ],
        "origin": []
    }


    auth_dir.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Ensured directory exists: {auth_dir}")

    auth_path = auth_dir / "auth.json"

    try:
        with open(auth_path, "w") as f:
            json.dump(state, f)
        logger.info(f"Auth state saved: {auth_path}")

    except Exception as e:
        logger.error(f"Failed to write auth state to file: {e}")
        raise

    return auth_path