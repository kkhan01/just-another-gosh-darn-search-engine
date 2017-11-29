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
    r = r.json()
    ret = []
    for suggestion in r['Similar']['Results']:
        sub = {}
        url = "www.google.com/search?q=%s" % suggestion['Name']
        sub['title'] = suggestion['Name']
        sub['description'] = 'This is a type of ' + suggestion['Type']
        sub['url'] = url
        ret.append(sub)
    return ret
        

    
