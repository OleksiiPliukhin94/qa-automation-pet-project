#Виносимо сюди логіку функцій
import requests
from settings import BASE_URL


def get_request_log(endpoint: str) -> requests:
    response = requests.get(BASE_URL+endpoint)
    return response
    #TODO написати логування