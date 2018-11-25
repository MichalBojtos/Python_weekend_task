import bin.filters as filters
import pandas


# changing JSON structure of IATA results to Dataframe
def output_iata(dt, json):
    iata = filters.iata(json)
    column_values = pandas.Series(iata)
    dt.insert(loc=0, column='IATA', value=column_values)


# changing JSON structure of Cities results to Dataframe
def output_cities(dt, json):
    cities = filters.cities(json)
    column_values = pandas.Series(cities)
    dt.insert(loc=0, column='Cities', value=column_values)


# changing JSON structure of Names of Airports results to Dataframe
def output_names(dt, json):
    airport_name = filters.airport_name(json)
    column_values = pandas.Series(airport_name)
    dt.insert(loc=0, column='Airport_name', value=column_values)


# changing JSON structure of coordinates results to Dataframe
def output_coords(dt, json):
    coordinates = filters.coords(json)
    column_values = pandas.Series(coordinates)
    dt.insert(loc=0, column='Coordinates', value=column_values)