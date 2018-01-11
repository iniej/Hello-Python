import requests
import os

key = os.environ['omdb Key']
base_url = 'http://www.omdbapi.com/'
Movie = input("What Movie name?")
Params = {‘apikey’ : key, ‘t’ : movie}
data = requests.get(base_url_params).json()
print(data)
print("rating for movie: ")
print(data['ratings'][0]['value'])
