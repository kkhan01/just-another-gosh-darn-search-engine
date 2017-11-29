import csv
import requests
import codecs

def youtube_search(search):
    reader = csv.DictReader(codecs.open('api_keys.csv','rU', 'utf-16'))
    reader.next()
    for row in reader:
        search_type = row['Type']
        key = row.get('API')
        if search_type == 'TasteDive':
            use_key = key
    api_url = "https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.channels.list?"
    payload = { 'part' : 'snippet',
                'q' : search,
                'type' : 'video',
                'videoCaption' : 'closedCaption',
                'key' : key}
    result = requests.get(api_url, params=payload)
    result = result.json()
    return result
