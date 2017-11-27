from flask import Flask, render_template, session, redirect, url_for, request, flash

def google_search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        key = reader['Google']
    return "http://www.google.com/customsearch/v1?key=%s&cx=001172072688314740745:fwbcfymikgm&q=%s" % (key, search)
