# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import random
import model

import requests #To access our API

# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    session["score"] = 0
    return render_template('index.html')

@app.route('/random')
def jeopardy_random():
    # Use jservice API/random to get 1 jeopardy clue
    response = requests.get('https://jservice.io/api/clues').json()
    index = random.randint(0, len(response))
    session['question'] = response[index]
    send = [response[index], session["score"]]
    return render_template('random_clue.html', data = send)

@app.route('/results', methods = ['GET', 'POST'])
def handle_results():
    if request.method == 'GET':
        return "You need to POST"
    else:
        form = request.form
        answer = form['answer']
        points = model.calc_points(session['question'], answer)
        session['score'] += points
        send = [session['question'], answer, points, session['score']]
        return render_template('results.html', data = send)
        