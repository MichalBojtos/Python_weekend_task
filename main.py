import bin.input_api_airports
import bin.filters

if __name__ == "__main__":

    get_uk_airport = bin.input_api_airports.InputApi()
    jsonData = get_uk_airport.get_api()
    filters = bin.filters

    iata = bin.filters.iata(jsonData)
    print(iata)

    cities = filters.cities(jsonData)
    print(cities)

    airportName = filters.airport_name(jsonData)
    print(airportName)

    coordinates = filters.coords(jsonData)
    print(coordinates)



