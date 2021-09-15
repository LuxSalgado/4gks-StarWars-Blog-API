"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#########################################################################  

@app.route('/character', methods=['GET'])
def get_character():
    query_character = Character.query.all()
    query_character = list(map(lambda x: x.serialize(), query_character))
    print(query_character)
    response_body = {
        "msg": "Hello, this is your GET /character response ",
        "character": query_character
    }
    return jsonify(response_body), 200

@app.route('/character/<int:id>', methods=['GET'])
def get_character_unico(id = None):
    query_character = Character.query.get(id)
    if not query_character:
        return "Personaje no existe", 401
    return jsonify(query_character.serialize()), 200

#########################################################################

@app.route('/planet', methods=['GET'])
def get_planet():
    query_planet = Planet.query.all()
    query_planet = list(map(lambda x: x.serialize(), query_planet))
    print(query_planet)
    response_body = {
        "msg": "Hello, this is your GET /planet response ",
        "planet": query_planet
    }
    return jsonify(response_body), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_planet_unico(id = None):
    query_planet = Planet.query.get(id)
    if not query_planet:
        return "Planeta no existe", 401
    return jsonify(query_planet.serialize()), 200

#########################################################################

@app.route('/user', methods=['GET'])
def get_user():
    query_user = User.query.all()
    query_user = list(map(lambda x: x.serialize(), query_user))
    response_body = {
        "msg": "Hello, this is your GET /planet response ",
        "user": query_user
    }
    return jsonify(response_body), 200

@app.route('/user/favorites', methods=['GET'])
def get_favorites():
    query_favorites = Favorite.query.all()
    query_favorites = list(map(lambda x: x.serialize(), query_favorites))
    response_body = {
        "msg": "Hello, this is your GET /planet response ",
        "favorites": query_favorites
    }
    return jsonify(response_body), 200

#########################################################################
# Post de planetas y personajes
@app.route('/favorite/planet/<int:id>', methods=['POST'])
def post_fav_planet(id = None):
 if request.method == 'POST':
    user_id = request.json.get("user_id", None) #Lo validamos, si no existe (no lo mandan) lo definnimos "None"
    character_id = request.json.get("character_id", None) 
    planet_id = id
    vehicle_id = request.json.get("vehicle_id", None)
    
    
    if not user_id:
        return jsonify({"msg":"Userid requerido"}), 401
    if character_id:
        return jsonify({"msg":"Solo puedes agregar a un favorito a la vez"}), 401
    if vehicle_id:
        return jsonify({"msg":"Solo puedes agregar a un favorito a la vez"}), 401
    
    favorite = Favorite()
    favorite.user_id = user_id
    favorite.character_id = character_id
    favorite.planet_id = planet_id
    favorite.vehicle_id = vehicle_id

    db.session.add(favorite)
    db.session.commit()

    response = {
        "msg": "Favorito agregado exitosamente"
    }
    return jsonify(response), 201 #Devuelvo en texto plano

@app.route('/favorite/character/<int:id>', methods=['POST'])
def post_fav_character(id = None):
 if request.method == 'POST':
    user_id = request.json.get("user_id", None) #Lo validamos, si no existe (no lo mandan) lo definnimos "None"
    character_id = id
    planet_id = request.json.get("planet_id", None) 
    vehicle_id = request.json.get("vehicle_id", None)
    
    
    if not user_id:
        return jsonify({"msg":"Userid requerido"}), 401
    if planet_id:
        return jsonify({"msg":"Solo puedes agregar a un favorito a la vez"}), 401
    if vehicle_id:
        return jsonify({"msg":"Solo puedes agregar a un favorito a la vez"}), 401
    
    favorite = Favorite()
    favorite.user_id = user_id
    favorite.character_id = character_id
    favorite.planet_id = planet_id
    favorite.vehicle_id = vehicle_id

    db.session.add(favorite)
    db.session.commit()

    response = {
        "msg": "Favorito agregado exitosamente"
    }
    return jsonify(response), 201 #Devuelvo en texto plano

#########################################################################
# Delete de planetas y personajes
@app.route('/favorite/planet/<int:id>', methods=['DELETE'])
def delete_fav_planet(id = None):
 if request.method == 'DELETE':
    favorite = Favorite.query.filter_by(planet_id=id).first()

    db.session.delete(favorite)
    db.session.commit()

    response = {
        "msg": "Favorito borrado"
    }
    return jsonify(response), 201 #Devuelvo en texto plano

@app.route('/favorite/character/<int:id>', methods=['DELETE'])
def delete_fav_character(id = None):
 if request.method == 'DELETE':
    favorite = Favorite.query.filter_by(character_id=id).first()

    db.session.delete(favorite)
    db.session.commit()

    response = {
        "msg": "Favorito borrado"
    }
    return jsonify(response), 201 #Devuelvo en texto plano

#########################################################################

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
