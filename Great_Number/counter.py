

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'thisissecret'



@app.route('/')
def index():
    session['class']= 'firstpage'
    print session['class']
    return render_template('index.html')
app.run(debug=True)
