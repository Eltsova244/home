
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return ("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    return