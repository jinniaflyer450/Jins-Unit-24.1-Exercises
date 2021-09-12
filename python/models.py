"""Models for the application for a fictional adoption agency."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    """A model that represents a pet animal."""