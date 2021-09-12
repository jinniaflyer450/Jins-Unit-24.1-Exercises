from flask import Flask, render_template, redirect, flash, url_for
from flask-sqlalchemy import SQLAlchemy
from flask-wtf import FlaskForm
from models import Pet
from forms import AddPetForm, EditPetForm

@app.route('/')
def show_home():
    """A view function that returns the homepage of the adoption website, which lists all pets in the database."""

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """A view function that returns a form to add a new pet on a GET request and submits the form to the
    database on a POST request."""

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details_and_edit(pet_id):
    """A view function that returns a page with details for the pet in the database with the id of pet_id and
    a form to edit this pet's details on a GET request. On a POST request, this view function submits the form."""