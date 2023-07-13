import datetime as dt
import requests
import pprint

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key.txt', 'r').read()
CITY = "London"

url = BASE_URL + "appid=" + API_KEY +"&q=" + CITY
response = requests.get(url).json()


def convert_kelvin_to_celsuis_farenheit(kelvin):
    celsuis = kelvin - 273.17
    fahrenheit = celsuis * (9/5) + 32
    return celsuis, fahrenheit



temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = convert_kelvin_to_celsuis_farenheit(temp_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}/{response['sys']['country']}: {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
print(f"Local Time in {CITY}: {dt.datetime.utcfromtimestamp(response['dt'])}")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at {sunrise_time} local time.")
print(f"Sun sets in {CITY} at {sunset_time} local time.\n")


'''
for key, value in response.items():
    print(key, value)
'''

