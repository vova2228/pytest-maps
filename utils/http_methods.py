import requests

"""Список HTTP методов"""

class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookies = ""

    @staticmethod
    def get(url):
        response = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        return response

    @staticmethod
    def post(url, body):
        response = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
        return response

    @staticmethod
    def put(url, body):
        response = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
        return response

    @staticmethod
    def delete(url, body):
        response = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
        return response
