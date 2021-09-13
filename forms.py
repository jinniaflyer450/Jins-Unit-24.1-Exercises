"""Forms for the application for a fictional adoption agency."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Pet
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FloatField

class AddPetForm(FlaskForm):
    """A form for adding a new pet to the adoption website's database."""
    name = StringField("Name")
    species = StringField("Species")
    availability = BooleanField("Available for adoption?")
    picture = StringField("Photo")
    age = FloatField("Age")
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """A form for editing a pet that is already in the adoption website's database."""