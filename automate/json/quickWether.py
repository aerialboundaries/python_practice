import json
import sys
import pprint

import requests


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
apiKey = '13c537300a9d520aedf35c54ff9112c1'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'\
      .format(location, apiKey)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
pprint.pprint(weatherData)

# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s: ' % (location))
print(w[0]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
