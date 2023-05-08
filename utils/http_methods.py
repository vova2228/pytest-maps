import requests

from utils.logger import Logger

"""Список HTTP методов"""


class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookies = ""

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        response = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(response)
        return response

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        response = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(response)
        return response

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        response = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(response)
        return response

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        response = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
        Logger.add_response(response)
        return response
