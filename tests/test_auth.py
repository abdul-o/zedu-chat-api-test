import requests
import os
from dotenv import load_dotenv
from jsonschema import validate
from tests.schemas import login_schema

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def test_login_success():
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": EMAIL, "password": PASSWORD}
    )

    data = response.json()

    #  Status code
    assert response.status_code == 200

    #  Field presence
    assert "data" in data
    assert "access_token" in data["data"]

    #  Data type
    assert isinstance(data["data"]["access_token"], str)

    #  Field value
    assert len(data["data"]["access_token"]) > 0

    # Message validation
    assert data["status"] == "success"

    #  Schema validation
    validate(instance=data, schema=login_schema)