from flask import Flask, render_template, session, redirect, url_for, request, flash

def google_search(search):
    return "http://www.google.com/search?start=0&num=10&output=xml_no_dtd&client=googlecsbe&cx=001172072688314740745:fwbcfymikgm&q=%s" % search
