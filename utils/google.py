import csv
import requests

def search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        key = reader['Google']
    api_url = "http://www.google.com/customsearch/v1?"
    payload = { 'key' : key,
                'cx' : '001172072688314740745:fwbcfymikgm',
                'q' : search}
    dictionary = requests.get(api_url, params=payload)
    ret = []
    for thing in dictionary:
        items = result['items']
        sub = [items['title'], items['snippet'], items['link']]
        ret.append(sub)
    return ret
