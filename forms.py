"""Forms for the application for a fictional adoption agency."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Pet
from flask_wtf import FlaskForm

class AddPetForm(FlaskForm):
    """A form for adding a new pet to the adoption website's database."""

class EditPetForm(FlaskForm):
    """A form for editing a pet that is already in the adoption website's database."""