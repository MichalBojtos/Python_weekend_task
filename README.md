# Python_weekend_task
This task is about getting information from the skypicker.com API and creating of specific result (IATA, Cities, Names of Airports, Coordinates).

More info about assignment: https://gist.github.com/fholec/ecc9c8a3bb82fdf3eabab66efb7c594b

## Project Structure:
```
Project
│   README.md
│   main.py    
└───bin
    │   filters.py
    |   input_api_airports.py
    │   json_to_dataframe.py
```
## Ways how to run the program
You can specify multiple options in the program:
 * **--help** - print help message
 * **--cities** - cities with airports
 * **--coords** - coordinates of each airport
 * **--iata** - IATA codes
 * **--names** - name of the airport
 * **--full** - print every detail from each airport

Examples of run:
```
$ python main.py
$ python main.py --help
$ python main.py --cities
$ python main.py --iata --cities
$ python main.py --coords
$ python main.py --full
```
## Output
Output data is in format DataFrame for better understanding.

## Questions?
If you require any further information, feel free to contact me. (michalbojtos@gmail.com)
