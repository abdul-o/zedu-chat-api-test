import requests
import os
from dotenv import load_dotenv
from jsonschema import validate
from tests.schemas import error_schema

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")


def test_login_wrong_password():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": EMAIL, "password": "wrongpass"}
    )

    data = response.json()

    assert response.status_code == 400
    assert "message" in data
    assert isinstance(data["message"], str)
    assert "invalid" in data["message"].lower()

    validate(instance=data, schema=error_schema)


def test_login_empty_email():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "", "password": "Password123!"}
    )

    data = response.json()

    assert response.status_code == 400
    assert "message" in data

    assert data["message"].lower() in ["validation failed", "invalid credentials"]

    validate(instance=data, schema=error_schema)


def test_login_empty_password():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": EMAIL, "password": ""}
    )

    data = response.json()

    assert response.status_code == 400
    assert "message" in data
    assert data["message"].lower() in ["validation failed", "invalid credentials"]

    validate(instance=data, schema=error_schema)


def test_login_invalid_email_format():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "invalidemail", "password": "Password123!"}
    )

    data = response.json()

    assert response.status_code == 400
    assert "message" in data


    assert data["message"].lower() in ["invalid credentials", "validation failed"]
    validate(instance=data, schema=error_schema)


def test_login_missing_fields():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={}
    )

    data = response.json()

    assert response.status_code == 400
    assert "message" in data
    assert data["message"].lower() in ["validation failed", "invalid credentials"]

    validate(instance=data, schema=error_schema)


def test_login_wrong_email():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "wrong@gmail.com", "password": "Password123!"}
    )

    data = response.json()

    assert response.status_code == 400
    assert "message" in data
    assert "invalid" in data["message"].lower()

    validate(instance=data, schema=error_schema)


def test_login_sql_injection():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "' OR 1=1 --", "password": "hack"}
    )

    data = response.json()

    assert response.status_code in [400, 401]
    assert "message" in data
    assert isinstance(data["message"], str)

    validate(instance=data, schema=error_schema)


def test_invalid_token_format():
    headers = {"Authorization": "Invalid token"}
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    data = response.json()

    assert response.status_code in [401, 403]
    assert "message" in data

    validate(instance=data, schema=error_schema)