import requests


class Weather:

    def __init__(self, url, query, key):
        self.url = url
        self.query = query
        self.key = key
        self.params = key + query

    def get_weather(self):
        response = requests.get(self.url + self.params)
        api_response = response.json()

        location = api_response['location']['name']
        temperature = api_response['current']['temperature']
        description = api_response['current']['weather_descriptions'][0]
        graphic_link = api_response['current']['weather_icons'][0]

        weather = {'location': location, 'temperature': temperature, 'description': description,
                   'graphic_link': graphic_link}

        return weather
