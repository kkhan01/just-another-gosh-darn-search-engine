from flask import Flask, render_template, session, redirect, url_for, request, flash

def news_search(search):
    return "https://newsapi.org/v2/top-headlines?sources=%s&apiKey=%s" % (search, key)
