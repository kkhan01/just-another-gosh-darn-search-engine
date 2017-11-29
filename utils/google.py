import csv

def google_search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        reader.next()
        for line in reader:
            if line['Type'] == 'Google':
                key = line.get('API_KEY')
        api_url = "http://www.google.com/customsearch/v1?"
        payload = { 'key' : key,
                    'cx' : '001172072688314740745:fwbcfymikgm',
                    'q' : search}
        r = requests.get(api_url, params=payload)
        r = r.json()
        ret = []
        for thing in r:
            items = result['items']
            sub = [items['title'], items['snippet'], items['link']]
            ret.append(sub)
        return ret
