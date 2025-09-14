import pytest

@pytest.mark.smoke
def test_get_list_user_status_code(get_request):
    assert get_request["response"].status_code == 200

@pytest.mark.smoke
def test_get_list_user_page_number(get_request):
    assert get_request["body"]["page"] == 2

@pytest.mark.smoke
def test_get_list_user_per_page_parameter(get_request):
    assert get_request["body"]["per_page"] == 6

@pytest.mark.smoke
def test_get_list_user_len_of_body(get_request):
    assert len(get_request["body"]["data"]) == 6

@pytest.mark.smoke
def test_get_list_user_total_parameter(get_request):
    assert get_request["body"]["total"] == 12








