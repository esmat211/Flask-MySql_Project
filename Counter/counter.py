

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'thisissecret'

def counter():
    try:
        session['counter'] +=1
    except KeyError:
        session['counter']= 1


@app.route('/')
def index():
    counter()
    return render_template("index.html")

@app.route('/reset', methods=['post'])
def reset():
    session.clear()
    return redirect('/')


@app.route('/generate', methods=['post'])
def generate():
    session['counter']+= 1
    return redirect('/')



app.run(debug=True)
