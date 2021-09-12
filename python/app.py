"""An application for a fictional pet adoption agency. Users can add various pets to a database and edit
existing pets as they are brought in or adopted."""

from flask import Flask, request, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask-wtf import FlaskForm
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'catdog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ob1wankenobi@localhost/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['WTF_CSRF_ENABLED'] = False

connect_db(app)
db.create_all()

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