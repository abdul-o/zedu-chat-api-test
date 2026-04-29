import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


# 1. Empty email and password
def test_login_empty_fields():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "", "password": ""}
    )
    assert response.status_code == 400


# 2. Null values
def test_login_null_values():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": None, "password": None}
    )
    assert response.status_code == 400


# 3. Extremely long email
def test_login_very_long_email():
    long_email = "a" * 200 + "@gmail.com"
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": long_email, "password": "Password123!"}
    )
    assert response.status_code in [400, 401]


# 4. Special characters input
def test_login_special_characters():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "!!!@@@###", "password": "$$$%%%"}
    )
    assert response.status_code == 400


# 5. Case sensitivity check
def test_login_email_case_sensitivity():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": os.getenv("EMAIL").upper(),
            "password": os.getenv("PASSWORD")
        }
    )
    # Some systems allow this, some don't → accept both valid outcomes
    assert response.status_code in [200, 400, 401]


# 6. Repeated login attempts (rate/consistency)
def test_multiple_login_requests():
    for _ in range(3):
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "email": os.getenv("EMAIL"),
                "password": os.getenv("PASSWORD")
            }
        )
        assert response.status_code == 200


# 7. Missing password field
def test_login_missing_password():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": os.getenv("EMAIL")}
    )
    assert response.status_code == 400


# 8. Missing email field
def test_login_missing_email():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"password": os.getenv("PASSWORD")}
    )
    assert response.status_code == 400

def test_login_whitespace_email():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "   ", "password": "Password123!"}
    )

    assert response.status_code == 400


def test_login_numeric_email():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "123456", "password": "Password123!"}
    )

    assert response.status_code == 400