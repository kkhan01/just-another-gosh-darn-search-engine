import csv

def youtube_search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        reader.next()
        for line in reader:
            if line['Type'] == 'Youtube':
                key = line.get('API_KEY')
        api_url = "https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.channels.list?"
        payload = { 'part' : 'snippet',
                    'q' : search,
                    'type' : 'video',
                    'videoCaption' : 'closedCaption',
                    'key' = key}
        result = requests.get(api_url, params=payload)
        result = result.json()
        ret = []
        for thing in result:
                link = 'https://www.youtube.com/watch?v=' + items['id']['videoId']
                items = result['items']['snippet']
                sub = [items['title'], items['description'], link]
                ret.append(sub)
        return ret
