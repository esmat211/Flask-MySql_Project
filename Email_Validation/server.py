
# import Flask
from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'Email_Validation')

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
#
# @app.route('/process', methods=['POST'])
# def submit():

@app.route('/', methods=['GET'])
def index():
    query = "SELECT * FROM email"
    email = mysql.query_db(query)
    return render_template('result.html', all_email=email)
# return redirect('/result.html')

@app.route('/email', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    if not EMAIL_REGEX.match(request.form['email_address']):
        flash("Invalid Email Address!")
    elif EMAIL_REGEX.match(request.form['email_address']):

        query = """INSERT INTO email (email_address)
             VALUES (:email_address)"""
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'email_address': request.form['email_address']
               }

        mysql.query_db(query, data)
        return redirect('index.html')
app.run(debug=True)
