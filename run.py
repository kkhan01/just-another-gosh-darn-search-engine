from flask import Flask, render_template, session, redirect, url_for, request, flash

run = Flask(__name__)

@run.route('/')
def route_root():
    '''
    type = request.form["type"]
    search = request.form["search"]
    if type == 'google':
        u = urllib2.urlopen('http://www.freegeoip.net/json/%s' % website)
        data_string = u.read()
        d = json.loads(data_string)
    '''
    return render_template('home.html')

@run.route('/about')
def route_about():
    return render_template('about.html')

if __name__ == "__main__":
    run.debug = True
    run.run()
