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
def index():
    return render_template("index.html")
