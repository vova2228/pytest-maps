from test_data.Test_Data import Test_Data
from utils.http_methods import Http_methods

"""Методы для тестирования Google maps api"""

base_url = "https://rahulshettyacademy.com"  # Базовый URL
key = "?key=qaclick123"  # Ключ query

address = Test_Data.address
new_address = Test_Data.new_address
lat = Test_Data.lat
lon = Test_Data.lon
phone_number = Test_Data.phone_number

class Google_maps_api:
    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():
        post_json_body = {
            "location": {
                "lat": lat,
                "lng": lon
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": phone_number,
            "address": address,
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_path = "/maps/api/place/add/json"  # Ресурс метода POST
        post_url = base_url + post_path + key

        post_response = Http_methods.post(post_url, post_json_body)
        print(post_url)
        print(post_response.text)
        return post_response

    """Метод для проверки новой локации"""
    @staticmethod
    def get_new_place(place_id):
        get_path = "/maps/api/place/get/json"  # Ресурс метода GET
        get_url = base_url + get_path + key + "&place_id=" + place_id
        print(get_url)

        get_response = Http_methods.get(get_url)
        print(get_response.text)
        return get_response

    """Метод для изменения новой локации"""
    @staticmethod
    def put_new_place(place_id):
        put_path = "/maps/api/place/update/json"  # Ресурс метода GET
        put_url = base_url + put_path + key
        print(put_url)

        put_json_body = {
            "place_id": place_id,
            "address": new_address,
            "key": "qaclick123"
        }

        put_response = Http_methods.put(put_url, put_json_body)
        print(put_response.text)
        return put_response

    @staticmethod
    def delete_place(place_id):
        delete_path = "/maps/api/place/delete/json"  # Ресурс метода DELETE
        delete_url = base_url + delete_path + key
        print(delete_url)

        delete_json_body = {
            "place_id": place_id
        }

        delete_response = Http_methods.put(delete_url, delete_json_body)
        print(delete_response.text)
        return delete_response
