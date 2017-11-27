from flask import Flask, render_template, session, redirect, url_for, request, flash

def news_search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        key = reader['News']
    return "https://newsapi.org/v2/top-headlines?apiKey=%s&sources=%s" % (key, search)
