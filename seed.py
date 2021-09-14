from models import db, Pet
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

def reset_database():
    db.drop_all()
    db.session.commit()
    db.create_all()
    db.session.commit()

def add_pets():
    fido = Pet(name="Fido", species="dog", availability=True)
    fifi = Pet(name="Fifi", species="cat", availability=False, age=2)
    baxter = Pet(name="Baxter", species="porcupine", availability=True, age=20)

    db.session.add_all([fido, fifi, baxter])
    db.session.commit()

reset_database()
add_pets()
