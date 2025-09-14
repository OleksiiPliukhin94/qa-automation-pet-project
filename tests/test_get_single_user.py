import pytest

@pytest.mark.smoke
def test_get_single_user_status_code(get_request_single_user):
    assert get_request_single_user["response"].status_code == 200

@pytest.mark.smoke
def test_get_single_user_id(get_request_single_user):
    assert get_request_single_user["body"]["data"]["id"] == 2

@pytest.mark.smoke
def test_get_singe_user_email(get_request_single_user):
    assert get_request_single_user["body"]["data"]["email"] == "janet.weaver@reqres.in"

@pytest.mark.smoke
def test_get_singe_user_fisrt_name(get_request_single_user):
    assert get_request_single_user["body"]["data"]["first_name"] == "Janet"

@pytest.mark.smoke
def test_get_singe_user_fisrt_name(get_request_single_user):
    assert get_request_single_user["body"]["data"]["last_name"] == "Weaver"

@pytest.mark.smoke
def test_get_single_user_avatar(get_request_single_user):
    avatar_url = get_request_single_user["body"]["data"]["avatar"]
    assert avatar_url.startswith("https://")

@pytest.mark.smoke
def test_get_single_user_support_url(get_request_single_user):
    support = get_request_single_user["body"]["support"]
    assert support["url"] == 'https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral'

@pytest.mark.smoke
def test_get_single_user_support_text(get_request_single_user):
    support = get_request_single_user["body"]["support"]
    assert support["text"] == "Tired of writing endless social media content? Let Content Caddy generate it for you."
