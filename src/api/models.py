from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    date_of_birth = db.Column(db.Date(), unique=False, nullable=False)
    latitude = db.Column(db.Float(), unique=False, nullable=False)
    longitude = db.Column(db.Float(), unique=False, nullable=False)
    profile_picture = db.Column(db.String(120), unique=False,)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "date_of_birth": self.date_of_birth,
            "profile_picture": self.profile_picture,
            # do not serialize the password, its a security breach
        }

class Nightclub(db.Model):
    night_club_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    latitude = db.Column(db.Float(), unique=False, nullable=False)
    longitude = db.Column(db.Float(), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    cover_photo = db.Column(db.String(120), unique=False, nullable=Flase)
    average_rating = db.Column(db.Float(), unique=False, nullable=False)

class Chatbox(db.Model):
    chatbox_id = db.Column(db.Integer, primary_key=True)
    