import pytest
from utils.auth import get_token

@pytest.fixture
def token():
    return get_token()