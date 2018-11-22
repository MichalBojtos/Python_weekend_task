import bin.input_api_airports
import bin.filters
import argparse


if __name__ == "__main__":

    get_uk_airport = bin.input_api_airports.InputApi()
    jsonData = get_uk_airport.get_api()
    filters = bin.filters

    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('--iata', action='store_true', help= 'IATA codes')
    parser.add_argument('--cities', action='store_true', help='cities with airports')
    parser.add_argument('--names', action='store_true', help = 'name of the airport')
    parser.add_argument('--coords', action='store_true', help='coordinates of each airport')
    parser.add_argument('--full', action='store_true', help='print every detail from each airport')

    args = parser.parse_args()

    if args.iata:
        iata = filters.iata(jsonData)
        print(iata)
    elif args.cities:
        cities = filters.cities(jsonData)
        print(cities)
    elif args.names:
        airportName = filters.airport_name(jsonData)
        print(airportName)
    elif args.coords:
        coordinates = filters.coords(jsonData)
        print(coordinates)
    elif args.full:
        iata = filters.iata(jsonData)
        print(iata)
        cities = filters.cities(jsonData)
        print(cities)
        airportName = filters.airport_name(jsonData)
        print(airportName)
        coordinates = filters.coords(jsonData)
        print(coordinates)


