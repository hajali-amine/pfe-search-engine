import json
from scrapping import scrap_data_to_load

f = open("index.json")
params = json.load(f)
scrap_data_to_load("http://localhost:5000/api", params)
