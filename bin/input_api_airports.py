from urllib.request import urlopen
import json
import requests


# communication with skypicker.com API and getting main JSON result
class InputApi:

        def __init__(self):
            self.locations = 'https://api.skypicker.com' \
                             '/locations?type=subentity&term=GB&locale=en-US&active_only=true' \
                             '&location_types=airport&limit=200&sort=name'

        def check_connection(self):
            url = self.locations
            timeout = 10
            try:
                _ = requests.get(url, timeout=timeout)
                print('API Connection - OK')
            except requests.ConnectionError:
                raise ValueError('API Connection - Fail')

        def get_api(self):
            response = urlopen(self.locations)
            data = json.load(response)
            return data
