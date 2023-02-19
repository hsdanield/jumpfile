import requests


def get_request(path):
    response = requests.get(path)

    if response.status_code == 200:
        return response

    return None
