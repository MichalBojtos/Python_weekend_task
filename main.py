import bin.input_api_airports
import bin.filters
import argparse
import pandas


def output_iata(dt, json):
    iata = filters.iata(json)
    column_values = pandas.Series(iata)
    dt.insert(loc=0, column='IATA', value=column_values)


def output_cities(dt, json):
    cities = filters.cities(json)
    column_values = pandas.Series(cities)
    dt.insert(loc=0, column='Cities', value=column_values)


def output_names(dt, json):
    airport_name = filters.airport_name(json)
    column_values = pandas.Series(airport_name)
    dt.insert(loc=0, column='Airport_name', value=column_values)


def output_coords(dt, json):
    coordinates = filters.coords(json)
    column_values = pandas.Series(coordinates)
    dt.insert(loc=0, column='Coordinates', value=column_values)


if __name__ == "__main__":

    get_uk_airport = bin.input_api_airports.InputApi()
    jsonData = get_uk_airport.get_api()
    filters = bin.filters
    df = pandas.DataFrame({})

    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('--iata', action='store_true', help='IATA codes')
    parser.add_argument('--cities', action='store_true', help='cities with airports')
    parser.add_argument('--names', action='store_true', help='name of the airport')
    parser.add_argument('--coords', action='store_true', help='coordinates of each airport')
    parser.add_argument('--full', action='store_true', help='print every detail from each airport')

    args = parser.parse_args()

    if args.iata:
        output_iata(df, jsonData)
    if args.cities:
        output_cities(df, jsonData)
    if args.names:
        output_names(df, jsonData)
    if args.coords:
        output_coords(df, jsonData)
    if args.full:
        output_iata(df, jsonData)
        output_cities(df, jsonData)
        output_names(df, jsonData)
        output_coords(df, jsonData)

    if df.empty:
        output_iata(df, jsonData)
        output_names(df, jsonData)
        print(df)
    else:
        print(df)
