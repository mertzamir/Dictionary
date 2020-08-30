from flask import Flask, session, redirect, url_for, render_template, request
from flask_session import Session
from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
import goslate
import requests

app = Flask(__name__)

# Check for environment variable
if not "postgres://xvqgrrhdrnnlxc:e9af57d1d766ba516dcb631e4cee8a1fe805f1ee4c4523babf1099e9c2f1ee37@ec2-34-248-165-3.eu-west-1.compute.amazonaws.com:5432/d702ham2elhgno":
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://xvqgrrhdrnnlxc:e9af57d1d766ba516dcb631e4cee8a1fe805f1ee4c4523babf1099e9c2f1ee37@ec2-34-248-165-3.eu-west-1.compute.amazonaws.com:5432/d702ham2elhgno"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'super secret key'
db.init_app(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).scalar()
        if user == None:
            user = User(username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("sign"))
        else:
            return render_template("error.html",message="User already exists")
    return render_template("register.html")

@app.route("/sign", methods=["POST", "GET"])
def sign():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).all()
        if user == []:
            return render_template("error.html",message="yow")
        else:
            user = user[0]
            if user.password != password:
                return_render_template("error.html",messsage="wrong password")
            session["user_id"] = user.id
            return redirect(url_for('search'),user_id = user.id)
    return render_template("sign.html")

@app.route("/search=<int:user_id>")
def search(user_id):
    return f"{user_id}"









