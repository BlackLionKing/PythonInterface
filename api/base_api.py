import requests


class BaseApi(object):
    def send(self, data):
        response = requests.request(**data)
        return response.json()
