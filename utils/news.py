import requests
import csv

def search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        key = reader['News']
    api_url = "https://newsapi.org/v2/everything"
    payload = {'key' : key, 'q' : search}
    r = requests.get(api_url, params = payload)
    return r.json()
