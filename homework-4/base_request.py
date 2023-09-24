import requests


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, params=None):
        url = self.base_url + path
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response

    def post(self, path, data=None, json=None):
        url = self.base_url + path
        response = self.session.post(url, data=data, json=json)
        response.raise_for_status()
        return response

    def put(self, path, data=None, json=None):
        url = self.base_url + path
        response = self.session.put(url, data=data, json=json)
        response.raise_for_status()
        return response

    def delete(self, path):
        url = self.base_url + path
        response = self.session.delete(url)
        response.raise_for_status()
        return response
