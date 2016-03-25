from flask import Flask, request, render_template, redirect
from flask_analytics import Analytics
import json

application = Flask(__name__)
Analytics(application)

application.config['ANALYTICS']['UNIVERSAL_ANALYTICS']['ACCOUNT'] = 'UA-17574902-4'

@application.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
    	params = request.args
        return render_template('home.html')
    return render_template('home.html')


@application.route('/<short_url>')
def redirect_short_url(short_url):
    return render_template('redirect.html',short_url=short_url)
    


if __name__ == '__main__':
	application.run()