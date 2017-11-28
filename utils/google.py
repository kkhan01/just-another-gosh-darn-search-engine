import csv

def search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        key = reader['Google']
    dictionary = "http://www.google.com/customsearch/v1?key=%s&cx=001172072688314740745:fwbcfymikgm&q=%s" % (key, search)
    ret = []
    for thing in dictionary:
        items = result['items']
        sub = [items['title'], items['snippet'], items['link']]
        ret.append(sub)
    return ret
