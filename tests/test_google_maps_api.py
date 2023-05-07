import json

from requests import Response
from utils.assertions import Assertions
from utils.API import Google_maps_api

"""Создание, изменение и удаление новой локации"""


class Test_create_new_place:

    def test_create_new_place(self):

        print("\n\nМетод POST")
        post_response: Response = Google_maps_api.create_new_place()
        post_response_json = post_response.json()
        place_id = post_response_json.get("place_id")
        Assertions.check_status_code(post_response, 200)
        Assertions.check_json_token(post_response, ['status', 'place_id', 'scope', 'reference', 'id'])

        print("\nМетод GET после создания новой локации")
        get_response: Response = Google_maps_api.get_new_place(place_id)
        Assertions.check_status_code(get_response, 200)
        Assertions.check_json_token(get_response, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print("\nМетод PUT")
        put_response: Response = Google_maps_api.put_new_place(place_id)
        Assertions.check_status_code(put_response, 200)
        Assertions.check_json_token(put_response, ['msg'])

        print("\nМетод GET после обновления локации")
        get_response: Response = Google_maps_api.get_new_place(place_id)
        Assertions.check_status_code(get_response, 200)
        Assertions.check_json_token(get_response, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print("\nМетод DELETE. Удаление локации...")
        delete_response: Response = Google_maps_api.delete_place(place_id)
        Assertions.check_status_code(delete_response, 200)
        Assertions.check_json_token(delete_response, ['status'])


        print("\nМетод GET после удаления локации")
        get_response: Response = Google_maps_api.get_new_place(place_id)
        Assertions.check_status_code(get_response, 404)
        Assertions.check_json_token(get_response, ['msg'])

        print("Тестирование изменения, удаления и создания новой локации прошло успешно")