from models import db, Pet
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

def reset_database():
    db.drop_all()
    db.session.commit()
    db.create_all()
    db.session.commit()

reset_database()
