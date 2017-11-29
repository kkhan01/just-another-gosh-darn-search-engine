import csv
import requests

def search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader: 
            search_type = line['Type']
            key = line.get('API_KEY')
            if search_type == 'TasteDive':
                use_key = key
        api_url = "https://tastedive.com/api/similar"
        payload = {'k' : use_key, 'q' : search}
        r = requests.get(api_url, params = payload, verify = False)
        return r.json()

