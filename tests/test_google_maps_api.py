from requests import Response

from test_data.Test_Data import Test_Data
from utils.assertions import Assertions
from utils.API import Google_maps_api

"""Создание, изменение и удаление новой локации"""

address = Test_Data.address
new_address = Test_Data.new_address
lat = Test_Data.lat
lon = Test_Data.lon
phone_number = Test_Data.phone_number

class Test_create_new_place:

    def test_create_new_place(self):

        print("\n\nМетод POST")
        post_response: Response = Google_maps_api.create_new_place()
        post_response_json = post_response.json()
        place_id = post_response_json.get("place_id")
        Assertions.check_status_code(post_response, 200)
        Assertions.check_json_token(post_response, ['status', 'place_id', 'scope', 'reference', 'id'])
        Assertions.check_json_key_value(post_response, "status", "OK")

        print("\nМетод GET после создания новой локации")
        get_response: Response = Google_maps_api.get_new_place(place_id)
        Assertions.check_status_code(get_response, 200)
        Assertions.check_json_token(get_response, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Assertions.check_json_key_value(get_response, "address", address)
        recieved_latitude = get_response.json().get("location").get("latitude")
        recieved_longitude = get_response.json().get("location").get("longitude")
        Assertions.check_json_key_value(get_response, float(recieved_latitude), lat)
        Assertions.check_json_key_value(get_response, float(recieved_longitude), lon)
        Assertions.check_json_key_value(get_response, "phone_number", phone_number)

        print("\nМетод PUT")
        put_response: Response = Google_maps_api.put_new_place(place_id)
        Assertions.check_status_code(put_response, 200)
        Assertions.check_json_token(put_response, ['msg'])
        Assertions.check_json_key_value(put_response, "msg", "Address successfully updated")

        print("\nМетод GET после обновления локации")
        get_response: Response = Google_maps_api.get_new_place(place_id)
        Assertions.check_status_code(get_response, 200)
        Assertions.check_json_token(get_response, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Assertions.check_json_key_value(get_response, "address", new_address)
        recieved_latitude = get_response.json().get("location").get("latitude")
        recieved_longitude = get_response.json().get("location").get("longitude")
        Assertions.check_json_key_value(get_response, float(recieved_latitude), lat)
        Assertions.check_json_key_value(get_response, float(recieved_longitude), lon)
        Assertions.check_json_key_value(get_response, "phone_number", phone_number)

        print("\nМетод DELETE. Удаление локации...")
        delete_response: Response = Google_maps_api.delete_place(place_id)
        Assertions.check_status_code(delete_response, 200)
        Assertions.check_json_token(delete_response, ['status'])
        Assertions.check_json_key_value(delete_response, "status", "OK")

        print("\nМетод GET после удаления локации")
        get_response: Response = Google_maps_api.get_new_place(place_id)
        Assertions.check_status_code(get_response, 404)
        Assertions.check_json_token(get_response, ['msg'])
        Assertions.check_json_by_search_value(get_response, "msg", "failed")

        print("\n\nТестирование создания, изменения и удаления новой локации прошло успешно")