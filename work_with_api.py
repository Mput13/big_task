from io import BytesIO
import requests
import sys

from spn_get import spn_finder


def get_map(cords: [str, str], spn: str):
    geocoder_request = \
        "http://geocode-maps.yandex.ru/1.x"
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": ','.join(cords),
        "spn": f"{spn},{spn}",
        "l": "map"
    }
    response = requests.get(map_api_server, params=map_params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_api_server)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


def get_map_by_request(string_request):
    list_request = string_request.text().split()
    geocoder_request = \
        "http://geocode-maps.yandex.ru/1.x"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": "+".join(list_request),
        "format": "json"
    }
    response = requests.get(geocoder_request, params=geocoder_params).json()
    cords = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
    spn = spn_finder(response)[0]
    get_map(cords, str(spn))
    return cords, spn
