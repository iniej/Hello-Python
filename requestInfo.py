# program that fetches data from a web server using an open API.

import requests
import os
key = 'c19d5e54'
base_url = 'http://www.omdbapi.com/'
Movie = input("What Movie name?")
Params = {'apikey' : key, 't' : movie}
data = requests.get(base_url, params).json()
print(data)
print("rating for movie: ")
print(data['ratings'][0]['value'])
