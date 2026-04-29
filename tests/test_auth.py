import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def test_login_success():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": EMAIL,
            "password": PASSWORD
        }
    )

    data = response.json()

    print(response.status_code)
    print(data)

    #  Status check
    assert response.status_code == 200

    #  Correct JSON structure check
    assert "data" in data
    assert "access_token" in data["data"]

    #  Token validation
    token = data["data"]["access_token"]
    assert isinstance(token, str)
    assert len(token) > 0

def test_login_response_structure():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": EMAIL, "password": PASSWORD}
    )

    data = response.json()

    assert "status" in data
    assert "message" in data
    assert data["status"] == "success"


def test_login_token_expiry_present():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": EMAIL, "password": PASSWORD}
    )

    data = response.json()

    assert "access_token_expires_in" in data["data"]