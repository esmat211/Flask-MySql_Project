from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html", phrase="hello", times=5)


@app.route('/ninjas')
def success():
    return render_template('ninjas.html')

# @app.route('/picture/pic')
# def success():
#     return render_template('pic.html')
app.run(debug=True)
