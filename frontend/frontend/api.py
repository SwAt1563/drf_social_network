from django.http import HttpResponse
from django.conf import settings
import requests


def get_method(request, url):
    host = settings.API_NETWORK_HOST
    port = settings.API_PORT
    url = f"http://{host}:{port}/{url}"
    header = {
        'Accept': 'application/json',
        "Content-Type": "application/json",
        'X-CSRFToken': request.COOKIES.get('csrftoken'),
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        result = dict(response.json())
        # just for change all the docker network to localhost
        for key, value in result.items():
            result[key] = str(value).replace(host, 'localhost')
        return result
    return None

def post_method(request, url, data):
    host = settings.API_NETWORK_HOST
    port = settings.API_PORT
    url = f"http://{host}:{port}/{url}"
    header = {
        'Accept': 'application/json',
        "Content-Type": "application/json",
        'X-CSRFToken': request.COOKIES.get('csrftoken'),
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    response = requests.post(url, headers=header, data=data)
    if response.status_code == 200:
        return response.json()
    return None


def put_method(request, url, data):
    host = settings.API_NETWORK_HOST
    port = settings.API_PORT
    url = f"http://{host}:{port}/{url}/"
    header = {
        'Accept': 'application/json',
        "Content-Type": "application/json",
        'X-CSRFToken': request.COOKIES.get('csrftoken'),
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }

    response = requests.put(url, headers=header, data=data)

    if response.status_code == 200:
        return response.json()
    return None