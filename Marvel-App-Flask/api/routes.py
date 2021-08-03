from flask import Blueprint, request, jsonify
from helpers import token_required, JSONEncoder
from models import db, User, Hero, hero_schema, heroes_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return { 'some': 'value'}

# CREATE ENDPOINT
@api.route('/heroes', methods = ['POST'])
@token_required
def create_hero(current_user_token):
    name = request.json['name']
    special_power = request.json['special_power']
    home_planet = request.json['home_planet']
    nemesis = request.json['nemesis']
    weakness = request.json['weakness']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    hero = Hero(name, special_power, home_planet, nemesis, weakness, user_token = user_token )

    db.session.add(hero)
    db.session.commit()

    response = hero_schema.dump(hero)
    return jsonify(response)




# RETRIEVE ALL ENDPOINTS

@api.route('/heroes', methods = ['GET'])
@token_required
def get_heroes(current_user_token):
    owner = current_user_token.token
    heroes = Hero.query.filter_by(user_token = owner).all()
    response = heroes_schema.dump(heroes)
    return jsonify(response)


# RETRIEVE ONE ENDPOINT
@api.route('/heroes/<id>', methods = ['GET'])
@token_required

def get_hero(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        hero = Hero.query.get(id)
        response = hero_schema.dump(hero)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401



# UPDATE ENDPOINT
@api.route('/heroes/<id>', methods = ['POST','PUT'])
@token_required

def update_hero(current_user_token,id):
    hero = Hero.query.get(id) # GET INSTANCE

    hero.name = request.json['name']
    hero.description = request.json['description']
    hero.user_token = current_user_token.token

    db.session.commit()
    response = hero_schema.dump(hero)
    return jsonify(response)


# DELETE ENDPOINT
@api.route('/heroes/<id>', methods = ['DELETE'])
@token_required

def delete_hero(current_user_token, id):
    hero = Hero.query.get(id)
    db.session.delete(hero)
    db.session.commit()
    response = hero_schema.dump(hero)
    return jsonify(response)