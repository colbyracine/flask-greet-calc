from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welc_home():
    return "welcome home"

@app.route('/welcome/back')
def welc_back():
    return "welcome back"