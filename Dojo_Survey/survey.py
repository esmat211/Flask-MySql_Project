from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'thisissecret'
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['post'])
def create_user():
	session['firstname'] = request.form['firstname']
	session['lastname'] = request.form['lastname']
	session['Location'] = request.form['Location']
	return redirect('/users')

@app.route('/users')
def results():
  return render_template("result.html")

app.run(debug=True)
