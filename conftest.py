import pytest
from methods import get_request_log


@pytest.fixture()
@pytest.fixture(scope="module")
def get_request():
    response = get_request_log(endpoint='/api/users?page=2')
    return response

