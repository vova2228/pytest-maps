"""Методы для проверки ответов запросов"""
import json

import pytest
from requests import Response

class Assertions:
    """Метод для проверки статус кода"""

    @staticmethod
    def check_status_code(response: Response, status_code: int):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно! Статус код ответа от сервера = " + str(response.status_code))
        else:
            print("Провал! Статус код ответа от сервера = " + str(response.status_code))

    """Метод для проверки наличия полей в ответе сервера"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все ключи присутствуют!")


    """Метод для проверки значений полей в ответе сервера"""
    @staticmethod
    def check_json_key_value(response: Response, json_key, expected_value):
        checking_value = response.json().get(json_key)
        assert checking_value == expected_value
        print(f'**{json_key}** содержит верное значение')


    """Метод для проверки значений полей в ответе сервера по заданному слову"""
    @staticmethod
    def check_json_by_search_value(response: Response, json_key, search_value):
        json_body = response.json()
        checking_json_key = json_body.get(json_key)
        if search_value in checking_json_key:
            print(f'Слово {search_value} содержится в **{json_key}**')
        else:
            print(f'Слово {search_value} отсутствует в **{json_key}**')
        assert search_value in checking_json_key
