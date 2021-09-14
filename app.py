"""An application for a fictional pet adoption agency. Users can add various pets to a database and edit
existing pets as they are brought in or adopted."""

from flask import Flask, request, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FloatField
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'catdog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ob1wankenobi@localhost/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['WTF_CSRF_ENABLED'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_home():
    """A view function that returns the homepage of the adoption website, which lists all pets in the database."""
    pets = Pet.query.all()
    for pet in pets:
        if pet.photo_url == None:
            pet.photo_url = url_for('static', filename='no_image.png')
            db.session.add(pet)
    db.session.commit()
    return render_template('showlist.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """A view function that returns a form to add a new pet on a GET request and submits the form to the
    database on a POST request."""
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, species=form.species.data, availability=form.availability.data, 
        photo_url=form.picture.data, age=form.age.data, notes=form.notes.data)
        if new_pet.photo_url == '':
            new_pet.photo_url = None
        if new_pet.age == '':
            new_pet.age = None
        if new_pet.notes == '':
            new_pet.notes = None
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added new pet named {new_pet.name}.")
        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_details_and_edit(pet_id):
    """A view function that returns a page with details for the pet in the database with the id of pet_id and
    a form to edit this pet's details on a GET request. On a POST request, this view function submits the form."""
    pet = Pet.query.get(pet_id)
    pet_for_form = {"picture": pet.photo_url, "notes": pet.notes, "availability": pet.availability}
    form = EditPetForm(obj=pet_for_form)
    if form.validate_on_submit():
        pet.availability = form.availability.data
        if form.picture.data == '':
            pet.photo_url = url_for('static', filename="no_image.png")
        else:
            pet.photo_url = form.picture.data
        pet.notes = form.notes.data
        db.session.add(pet)
        db.session.commit()
        flash(f"Edited pet named {pet.name}.")
        return redirect(f'/{pet.id}')
    else:
        return render_template('detailsandedit.html', pet=pet, form=form)
