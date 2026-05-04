import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def get_token():
    # Validate environment variables
    assert BASE_URL is not None, "BASE_URL not set in .env"
    assert EMAIL is not None, "EMAIL not set in .env"
    assert PASSWORD is not None, "PASSWORD not set in .env"

    url = f"{BASE_URL}/auth/login"

    response = requests.post(
        url,
        json={
            "email": EMAIL,
            "password": PASSWORD
        },
        timeout=10
    )

    # Debug information
    print(f"LOGIN URL: {url}")
    print(f"STATUS: {response.status_code}")
    print(f"RESPONSE: {response.text}")

    # Validate response
    assert response.status_code == 200, f"Login failed: {response.text}"

    data = response.json()

    # Validate structure
    assert "data" in data, f"'data' key missing: {data}"
    assert "access_token" in data["data"], f"'access_token' missing: {data}"

    token = data["data"]["access_token"]

    # Final validation
    assert isinstance(token, str) and len(token) > 0, "Invalid token"
    assert BASE_URL is not None, "BASE_URL is not set"
    return token