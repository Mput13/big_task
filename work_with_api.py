from io import BytesIO
import requests
import sys


def get_map(cords: [str, str], spn: [str, str]):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": ",".join(cords),
        "spn": ",".join(spn),
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


print(get_map(["37", "37"], ["0.002", "0.002"]))
