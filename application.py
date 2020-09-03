from flask import Flask, session, redirect, url_for, render_template, request
from flask_session import Session
from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
from email import * 
import requests
import time
import datetime as dt
from googletrans import Translator

#included email code below due to the scoping issues on send_email()
import datetime as dt
import time
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(user):
    #create the smpt server and login
    dict_email = 'dark_blue9299@hotmail.com' #fill in w/ your email
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.ehlo()
    #context = ssl.create_default_context() #create secure SSL context
    server.starttls()
    server.login(dict_email, 'askimasli12') #replace password

    #create message object
    msg = MIMEMultipart()
    
    #message template
    message = "Your Vocabulary List:\n"
    for word in user.words:
        word.count -= 1
        print("{} : {}".format(word.text, word.count))
            
        #TODO 
        #remove the word from words list if the count is < 0
        
        if word.count >= 0:
            message += (word.text + " -> " + word.translated + "\n")
    
    #setup the parameters
    msg['From'] = dict_email
    msg['To'] = user.username #fetched from user object
    msg['Subject'] = "Don't Forget To Skim Through!"

    #add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    #send the message via the server
    server.send_message(msg)
    print("mail sent")
    del msg

    #terminate the SMTP session and close connection
    server.quit()

def send_email_at(send_time, to_email):
    time.sleep(send_time.timestamp() - time.timestamp())
    send_email(to_email)
    print('email sent')

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
            return redirect(url_for('search',user_id = user.id))
    return render_template("sign.html")

@app.route("/search=<int:user_id>",methods=["POST","GET"])
def search(user_id):
    user = User.query.get(session["user_id"])
    words = user.words
    if request.method == "POST":
        text = request.form.get("text")
        translator = Translator()
        translation = translator.translate(text, dest="tr")
        translated = translation.text
        print(translated)

        #send email if there are at least 5 word searched
        user.add_word(text,translated)
        print(len(user.words))
        if len(user.words) % 5 == 0:
            send_email(user)
    return render_template("search.html",user=user)







