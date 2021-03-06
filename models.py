from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_PIC = 'https://thumbs.dreamstime.com/z/avatar-dog-avatar-dog-white-background-vector-illustration-105121614.jpg'

class Pet(db.Model):
    """Pet Model"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=DEFAULT_PIC)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Pet {self.name} {self.species} {self.photo_url} {self.age} {self.notes} {self.available}>"


