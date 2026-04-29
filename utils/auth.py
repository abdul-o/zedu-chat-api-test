import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def get_token():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": EMAIL,
            "password": PASSWORD
        }
    )

    assert response.status_code == 200, "Login failed"

    data = response.json()

    # IMPORTANT: handle possible response structure
    token = data.get("token") or data.get("access_token")

    assert token is not None, "Token not found in response"

    return token