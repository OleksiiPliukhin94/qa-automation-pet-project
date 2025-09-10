import pytest

@pytest.mark.smoke
def test_get_list_user_status_code(get_request):
    assert get_request.status_code == 200

#TODO зробити 10 тестів

@pytest.mark.smoke
def test_get_list_user_(get_request):
    assert get_request.status_code == 200








