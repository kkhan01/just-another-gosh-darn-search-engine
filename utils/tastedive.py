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
        url = "https://www.google.com/search?q=%s" % suggestion['Name']
        sub['title'] = suggestion['Name']
        sub['description'] = suggestion['Name'] + ' is a ' + suggestion['Type']
        sub['url'] = url
        ret.append(sub)
    if len(ret) == 0:
        sub = {}
        sub['title'] = "Sorry, I haven't heard of " + search
        sub['description'] = "Please don't click the link. Move on to your next search."
        ret.append(sub)
    return ret
        

    
