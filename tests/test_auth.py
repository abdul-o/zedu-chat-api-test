import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

def test_login_success():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": os.getenv("EMAIL"),
            "password": os.getenv("PASSWORD")
        }
    )

    assert response.status_code == 200
    assert "token" in response.json() or "access_token" in response.json()