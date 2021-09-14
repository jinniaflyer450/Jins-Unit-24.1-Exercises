"""Forms for the application for a fictional adoption agency."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Pet
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf

class AddPetForm(FlaskForm):
    """A form for adding a new pet to the adoption website's database."""
    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine")], 
    validators=[AnyOf(["dog", "cat", "porcupine"])])
    availability = BooleanField("Available for adoption?")
    picture = StringField("Photo", validators=[Optional(), URL("Photo source must be a URL.")])
    age = FloatField("Age (between 0 and 30)", 
    validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30 years old.")])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """A form for editing a pet that is already in the adoption website's database."""