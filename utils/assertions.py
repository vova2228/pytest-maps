"""Методы для проверки ответов запросов"""
import json
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
    def check_json_token(response: Response, expected_result):
        token = json.loads(response.text)
        assert list(token) == expected_result
        print("Все поля присутствуют!")