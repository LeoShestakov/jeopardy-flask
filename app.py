# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import random

import requests #To access our API

# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    session["name"] = "Leo"
    return render_template('index.html')

@app.route('/random')
def jeopardy_random():
    # Use jservice API/random to get 1 jeopardy clue
    response = requests.get('https://jservice.io/api/clues').json()
    index = random.randint(0, len(response))
    return render_template('random_clue.html', data = response[index])