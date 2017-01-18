from flask import Flask
app = flask( __name__ )
@app.route('/')

def hello_world():
    return 'hello world'
app.run(debug=true)
