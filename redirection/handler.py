import requests

def validate_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except Exception as e:
        raise e