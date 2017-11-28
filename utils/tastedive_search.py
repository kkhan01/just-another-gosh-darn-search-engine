from flask import Flask, render_template, session, redirect, url_for, request, flash

def tastedive_search(search):
    with open ('api_keys.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        key = reader['TasteDive']
    return "https://tastedive.com/api/similar?k=%s&q=%s" % (key, search)

