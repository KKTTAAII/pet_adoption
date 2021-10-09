from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form to add a new pet"""
    name = StringField("Name", validators=[InputRequired(message="Name can't be blank")])
    species = RadioField("Species", choices=[("cat", "Cat"),  ("dog", "Dog"),  ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Age can't be blank")])
    notes = StringField("Notes", validators=[Optional()])
