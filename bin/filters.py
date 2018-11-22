def iata(json):
    iata_code = []
    for i in range(len(json['locations'])):
        iata_code.append(json['locations'][i]['id'])
    return iata_code


def cities(json):
    name = []
    for i in range(len(json['locations'])):
        name.append(json['locations'][i]['city']['name'])
    return name


def airport_name(json):
    airport = []
    for i in range(len(json['locations'])):
        airport.append(json['locations'][i]['name'])
    return airport


def coords(json):
    coordinates = []
    for i in range(len(json['locations'])):
        latitude = json['locations'][i]['location']['lat']
        longitude = json['locations'][i]['location']['lon']
        coordinates.append([str(latitude) + ", " + str(longitude)])
    return coordinates