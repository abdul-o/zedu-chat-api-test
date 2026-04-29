import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")


def test_login_wrong_password():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": EMAIL, "password": "wrongpass"}
    )
    assert response.status_code == 400


def test_login_empty_email():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "", "password": "Password123!"}
    )
    assert response.status_code == 400


def test_login_empty_password():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": EMAIL, "password": ""}
    )
    assert response.status_code == 400


def test_login_invalid_email_format():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "invalidemail", "password": "Password123!"}
    )
    assert response.status_code == 400


def test_login_missing_fields():
    response = requests.post(f"{BASE_URL}/auth/login", json={})
    assert response.status_code == 400

def test_login_wrong_email():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "wrong@gmail.com", "password": "Password123!"}
    )

    assert response.status_code == 400


def test_login_sql_injection():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "' OR 1=1 --", "password": "hack"}
    )

    assert response.status_code in [400, 401]


def test_invalid_token_format():
    headers = {"Authorization": "Invalid token"}
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code in [401, 403]