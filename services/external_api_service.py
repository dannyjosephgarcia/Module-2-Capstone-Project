import requests

class ExternalAPIService:
    def __init__(self, external_url):
        self.external_url = external_url

    def call_external_api(self, name, salary, age):
        request = {'name': name, 'salary': salary, 'age': age}
