import csv
import requests
import codecs

def google_search(search):
    reader = csv.DictReader(codecs.open('api_keys.csv','rU', 'utf-16'))
    for row in reader:
        search_type = row['Type']
        key = row.get('API')
        if search_type == 'Google':
            use_key = key
    api_url = "http://www.google.com/customsearch/v1"
    payload = { 'key' : use_key,
                'cx' : '001172072688314740745:fwbcfymikgm',
                'q' : search}
    r = requests.get(api_url, params=payload)
    return r.json()
    '''ret = []
    for thing in dictionary:
        items = result['items']
        sub = [items['title'], items['snippet'], items['link']]
        ret.append(sub)
    return ret'''
