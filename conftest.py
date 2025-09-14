import pytest
from methods import get_request_log


@pytest.fixture(scope="module")
def get_request():
    response = get_request_log(endpoint='/api/users?page=2')
    return {
        "response": response,
        "body": response.json()
    }

@pytest.fixture(scope="module")
def get_request_single_user():
    response = get_request_log(endpoint='/api/users/2')
    return {
        "response": response,
        "body": response.json()
    }

