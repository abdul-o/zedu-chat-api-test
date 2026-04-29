import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def test_get_profile_success(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 200
    assert "data" in response.json()


def test_get_profile_without_token():
    response = requests.get(f"{BASE_URL}/users/me")

    assert response.status_code in [401, 403]


def test_get_profile_invalid_token():
    headers = {"Authorization": "Bearer invalidtoken"}
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code in [401, 403]

def test_profile_contains_email(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    data = response.json()

    assert "email" in data["data"]["user"]


def test_profile_contains_user_id(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    data = response.json()

    assert "data" in data
    assert "user" in data["data"]
    assert "id" in data["data"]["user"]
    assert isinstance(data["data"]["user"]["id"], str)
