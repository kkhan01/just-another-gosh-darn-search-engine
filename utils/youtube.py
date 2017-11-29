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
    api_url = "https://www.googleapis.com/youtube/v3/search?"
    payload = { 'part' : 'snippet',
                'q' : search,
                'type' : 'video',
                'videoCaption' : 'closedCaption',
                'key' : key}
    result = requests.get(api_url, params=payload)
    result = result.json()
    ret = []
    for video in result['items']:
        sub = {}
        url = 'https://www.youtube.com/watch?v=' + video['id']['videoId']
        sub['title'] = video['snippet']['title']
        sub['description'] = video['snippet']['description']
        sub['url'] = url
        ret.append(sub)
    return ret
