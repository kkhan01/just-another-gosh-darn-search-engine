import csv

def search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        key = reader['TasteDive']
        api_url = "https://tastedive.com/api/similar"
        payload = {'k' : key, 'q' : search}
        r = requests.get(api_url, params = payload)
        return r.json()

