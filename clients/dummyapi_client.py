import requests


class DummyAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def update_database(self, request, id):
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.39.0',
            'Accept': '*/*'
        }
        response = requests.put(self.base_url + f'/api/v1/update/{id}',
                                json=request,
                                headers=headers)
        return response.status_code
