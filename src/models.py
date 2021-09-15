from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(120), unique=False, nullable=False)
    gravity = db.Column(db.String(120), nullable=False)
    population = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "Planeta "+self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    eye_color = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet', lazy=True, uselist=False)

    def __repr__(self):
        return "Personaje "+self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "planet_id": self.planet_id
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), nullable=False)
    length = db.Column(db.String(120), nullable=False)
    passengers = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "Vehiculo "+self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "length": self.length,
            "passengers": self.passengers
            # do not serialize the password, its a security breach
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return "Usuario "+self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
            # do not serialize the password, its a security breach
        }
    
class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    user = db.relationship('User', lazy=True, uselist=False)
    character = db.relationship('Character', lazy=True, uselist=False)
    vehicle = db.relationship('Vehicle', lazy=True, uselist=False)
    planet = db.relationship('Planet', lazy=True, uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "vehicle_id": self.vehicle_id,
            "planet_id": self.planet_id
            # do not serialize the password, its a security breach
        }


    """ class People(db.Model):
        __tablename__ = 'people'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(120), unique=True, nullable=False)
        #planets = db.Column(db.String(120), unique=False, nullable=False)
        planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
        planet = db.relationship ('Planet', lazy=True, uselist=True)

    def __repr__(self):
        return 'Planeta %r' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "planet_id": self.planet_id,
            "planet": self.planet
            # do not serialize the password, its a security breach
        } """