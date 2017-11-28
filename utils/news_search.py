from flask import Flask, render_template, session, redirect, url_for, request, flash

def news_search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        key = reader['News']
    dictionary = "https://newsapi.org/v2/top-headlines?apiKey=%s&sources=%s" % (key, search)
    ret = []
    for news in dictionary:
        sub = [news['title'], news['description'], news['url']]
        ret.append(sub)
    return ret
