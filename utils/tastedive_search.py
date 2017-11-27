from flask import Flask, render_template, session, redirect, url_for, request, flash

def tastedive_search(search):
    return "https://tastedive.com/api/similar?q=%s" % search
