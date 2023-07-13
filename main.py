import datetime as dt
import requests
import pprint

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key.txt', 'r').read()
CITY = "London"

url = BASE_URL + "appid=" + API_KEY +"&q=" + CITY
response = requests.get(url).json()

print(response)