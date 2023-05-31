from flask import Flask
import requests, json

def populate():
    response = requests.get('https://api.gbif.org/v1/occurrence/search?limit=50')
    data = response.json()
    with open('occurrence.json', 'w') as f:
        json.dump(data, f)

    response = requests.get('https://api.gbif.org/v1/species?limit=50') 
    data = response.json()
    with open('species.json', 'w') as f:
        json.dump(data, f)


populate()
