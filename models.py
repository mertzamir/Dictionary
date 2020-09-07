from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    words = db.relationship("Word", backref="users", lazy=True)

    def add_word(self, text, translated):
        w = Word(text=text, translated=translated, count= 3,user_id=self.id)
        db.session.add(w)
        db.session.commit()
        return

    def rm_word(self, word):
        db.session.delete(word)
        db.session.commit()
        return

class Word(db.Model):
    __tablename__ = "words"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    translated = db.Column(db.String)
    count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),nullable=False)

    def decrement(self):
        self.count -= 1
        db.session.commit()
        return
