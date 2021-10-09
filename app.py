from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "evieiscutie"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def show_homepage():
    """Show the homepage with all pets"""
    all_pets = Pet.query.all()
    return render_template("home.html", all_pets=all_pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """Show add pet form"""
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} has been added to the community!")
        return redirect("/")
    else:
        return render_template("form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Show pet details with a form that a user can edit"""
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    # import the choices to fill the form as well
    form.species.choices = [("cat", "Cat"),  ("dog", "Dog"),  ("porcupine", "Porcupine")]

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()

        flash(f"{pet.name}'s info has been updated!")
        return redirect("/")
    else:
        return render_template("details.html", form=form, pet=pet)   