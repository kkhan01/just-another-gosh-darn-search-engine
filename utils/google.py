import csv
import requests
import codecs

def google_search(search):
    reader = csv.DictReader(codecs.open('api_keys.csv','rU', 'utf-16'))
    for row in reader:
        search_type = row['Type']
        key = row.get('API')
        if search_type == 'News':
            use_key = key
    api_url = 'https://www.googleapis.com/customsearch/v1'
    payload = { 'key' : use_key,
                'cx' : '001172072688314740745:fwbcfymikgm',
                'q' : search}
    r = requests.get(api_url, params=payload)
    r = r.json()
    ret = []
    return r
