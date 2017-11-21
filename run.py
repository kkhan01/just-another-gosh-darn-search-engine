from flask import Flask, render_template, session, redirect, url_for, request, flash
    
@app.route('/')
def route_root():
    return render_template('home.html')

@app.route('/about')
def route_about():
    "type = request.form["type"]
    search = request.form["search"]
    if type == 'google'
    u = urllib2.urlopen('http://www.freegeoip.net/json/%s' % website)
    data_string = u.read()
    d = json.loads(data_string)"
    return render_template('about.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
