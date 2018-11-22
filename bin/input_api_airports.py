from urllib.request import urlopen
import json


class InputApi:

        def __init__(self):
            self.locations = 'https://api.skypicker.com' \
                             '/locations?type=subentity&term=GB&locale=en-US&active_only=true' \
                             '&location_types=airport&limit=200&sort=name'

        def get_api(self):
            response = urlopen(self.locations)
            data = json.load(response)
            return data
