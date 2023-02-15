def spn_finder(json):
    lower_corner = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
        'lowerCorner'].split()
    upper_corner = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
        'upperCorner'].split()
    return float(upper_corner[0]) - float(lower_corner[0]), float(upper_corner[1]) - float(lower_corner[1])