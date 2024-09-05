import requests

def validate_url(url):
    try:

        if len(url) > 2048:
            raise Exception("URL too long")

        with requests.get(url) as response:
            if response.status_code != 200:
                raise Exception("Invalid URL")
    
    except Exception as e:
        raise e