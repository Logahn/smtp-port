#!/usr/bin/env python3

from requests.auth import HTTPBasicAuth
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()


longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_coordinates = (latitude, longitude)

print(f"ISS cordinates: {iss_coordinates}")




# url = 'http://api.weatherapi.com/v1/current.json'
# auth = HTTPBasicAuth('api_key', 'd9b36158fd6c4ba181f141438220507')
# weather_api = requests.get(url,  auth=auth)
# weather_api.raise_for_status()
# weather_data = weather_api.json()
# print(weather_data)

