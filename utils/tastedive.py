import csv
import requests
import codecs

def tastedive_search(search):
    reader = csv.DictReader(codecs.open('api_keys.csv','rU', 'utf-16'))
    for row in reader:
        search_type = row['Type']
        key = row.get('API')
        if search_type == 'TasteDive':
            use_key = key
    api_url = "https://tastedive.com/api/similar"
    payload = {'k' : use_key, 'q' : search}
    r = requests.get(api_url, params = payload)
    return r.json()

    
