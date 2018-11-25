# filtering of main JSON - IATA
def iata(json):
    iata_code = []
    for i in range(len(json['locations'])):
        iata_code.append(json['locations'][i]['id'])
    return iata_code


# filtering of main JSON - Cities
def cities(json):
    name = []
    for i in range(len(json['locations'])):
        name.append(json['locations'][i]['city']['name'])
    return name


# filtering of main JSON - Name of Airports
def airport_name(json):
    airport = []
    for i in range(len(json['locations'])):
        airport.append(json['locations'][i]['name'])
    return airport


# filtering of main JSON - Coordinates
def coords(json):
    coordinates = []
    for i in range(len(json['locations'])):
        latitude = json['locations'][i]['location']['lat']
        longitude = json['locations'][i]['location']['lon']
        coordinates.append([str(latitude) + ", " + str(longitude)])
    return coordinates
