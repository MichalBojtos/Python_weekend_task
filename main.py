import bin.input_api_airports as api_airports
import bin.json_to_dataframe as json_to_df
import argparse
import pandas


if __name__ == "__main__":

    # main variables
    get_uk_airport = api_airports.InputApi()
    get_uk_airport.check_connection()
    jsonData = get_uk_airport.get_api()
    df = pandas.DataFrame({})

    # use the argparse library for define of user options
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('--iata', action='store_true', help='IATA codes')
    parser.add_argument('--cities', action='store_true', help='cities with airports')
    parser.add_argument('--names', action='store_true', help='name of the airport')
    parser.add_argument('--coords', action='store_true', help='coordinates of each airport')
    parser.add_argument('--full', action='store_true', help='print every detail from each airport')

    args = parser.parse_args()

    # logic for input options
    if args.iata:
        json_to_df.output_iata(df, jsonData)
    if args.cities:
        json_to_df.output_cities(df, jsonData)
    if args.names:
        json_to_df.output_names(df, jsonData)
    if args.coords:
        json_to_df.output_coords(df, jsonData)
    if args.full:
        json_to_df.output_iata(df, jsonData)
        json_to_df.output_cities(df, jsonData)
        json_to_df.output_names(df, jsonData)
        json_to_df.output_coords(df, jsonData)

    # logic for printing of output
    if df.empty:
        json_to_df.output_iata(df, jsonData)
        json_to_df.output_names(df, jsonData)
        print(df)
    else:
        print(df)
