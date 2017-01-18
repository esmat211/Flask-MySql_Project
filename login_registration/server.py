from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'login_registration')
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql= MySQLConnector(app, 'login')
# flash is part of session and requires secret_key
app.secret_key = 'password'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)


name = re.compile (r'^[a-zA-Z]')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['post'])
def register():
    error = 0
    if len(request.form['first_name']) <2:
        error += 1
        flash("need more characters")
    elif not name.match(request.form['first_name']):
        error += 1
        flash('no numbers allowed in name')
    if len(request.form['last_name']) <2:
        error += 1
        flash("need more characters")
    elif not name.match(request.form['last_name']):
        error += 1
        flash('no numbers allowed in name')
    if not EMAIL_REGEX.match(request.form['email']):
        error += 1
        flash('email is not valid!')

    if len(request.form['password'])< 0:
        error += 1
        flash('password needs to be 9 charakcters or more !')
    if request.form['password'] != request.form['confirm']:
        error += 1
        flash(' password is not match!')
    if error == 0:
        hashed = bcrypt.generate_password_hash(request.form['password'])
        query = 'INSERT INTO USERS (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw, NOW(), NOW())'
        data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'pw': hashed }
        mysql.query_db(query, data)
        return redirect('login_info')
    return redirect('/')

@app.route('/login', methods = ['post'])
def login():
    error = 0
    query = 'SELECT id, password FROM users WHERE email = "{}"'.format(request.form['email'])
    user = mysql.query_db(query)
    print user

    if len(user) < 1:
        flash('Email is not exist')
        error += 1
    elif not bcrypt.check_password_hash(user[0]['password'], request.form['password']):
        flash('wrong password')
        error += 1
    elif error == 0:
        return redirect('/')

    return redirect('/')
@app.route('/login_info')
def login_info():
    return render_template('login_info.html')

app.run(debug=True)
