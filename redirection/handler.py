import requests

def validate_url(url):
    try:

        if len(url) > 2048:
            raise Exception("URL too long")

        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Invalid URL")
    
    except Exception as e:
        raise e