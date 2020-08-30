from flask import Flask, render_template, request,redirect, url_for
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://xvqgrrhdrnnlxc:e9af57d1d766ba516dcb631e4cee8a1fe805f1ee4c4523babf1099e9c2f1ee37@ec2-34-248-165-3.eu-west-1.compute.amazonaws.com:5432/d702ham2elhgno"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route

if __name__ == "__main__":
    app.run(debug=True)
