import requests
import csv
import codecs

def news_search(search):
    reader = csv.DictReader(codecs.open('api_keys.csv','rU', 'utf-16'))
    for row in reader:
        search_type = row['Type']
        key = row.get('API')
        if search_type == 'News':
            use_key = key
    print use_key
    api_url = "https://newsapi.org/v2/everything"
    payload = {'apikey' : use_key, 'q' : search}
    r = requests.get(api_url, params = payload)
    print r.url
    return r.json()
