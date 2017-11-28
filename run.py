from flask import Flask, render_template, session, redirect, url_for, request, flash

run = Flask(__name__)

@run.route('/')
def route_root():
    '''
    type = request.form["search-dest"]
    search = request.form["search-term"]
    if type == 'google':
        u = urllib2.urlopen('http://www.freegeoip.net/json/%s' % website)
        data_string = u.read()
        d = json.loads(data_string)
    if type == 'tastedive':
    if type == 'youtube':
    if type == 'news':
    '''
    return render_template('home.html')

@run.route('/about')
def route_about():
    return render_template('about.html')

@run.route('/getresults')
def route_getresults():
    return render_template('home.html')

@run.route('/results')
def route_results():
    return render_template('home.html')

if __name__ == "__main__":
    run.debug = True
    run.run()
