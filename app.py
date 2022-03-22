from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eonmgsqntxobbx:1071ab481be126ef1e6460e41704771d88f6119fa6e463f45d81448d0cedef00@ec2-44-194-92-192.compute-1.amazonaws.com:5432/d8vccq1195boo7'

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)


class Character(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    pname = db.Column(db.String, nullable=False)
    cname = db.Column(db.String, nullable=False)
    pclass = db.Column(db.String, nullable=False)
    race = db.Column(db.String, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String, nullable=False)
    basespeed = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    alignment  = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    biography = db.Column(db.String, nullable=False)
    copper = db.Column(db.Integer, nullable=False)
    silver = db.Column(db.Integer, nullable=False)
    gold = db.Column(db.Integer, nullable=False)
    platinum = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)

    def __init__(self, pname, cname, pclass, race, height, weight, gender, age, size, basespeed, level, alignment, description, biography, copper, silver, gold, platinum, strength, dexterity, constitution, intelligence, wisdom, charisma, hp):
        self.pname = pname
        self.cname = cname
        self.pclass = pclass
        self.race = race
        self.height = height
        self.weight = weight
        self.gender = gender
        self.age = age
        self.size = size
        self.basespeed = basespeed
        self.level = level
        self.alignment = alignment
        self.description = description
        self.biography = biography
        self.copper = copper
        self.silver = silver
        self.gold = gold
        self.platinum = platinum
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hp = hp

class CharacterSchema(ma.Schema):
    class Meta():
        fields = ("id", "pname", "cname", "pclass", "race", "height", "weight", "gender", "age", "size", "basespeed", "level", "alignment", "description", "biography", "copper", "silver", "gold", "platinum", "strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma", "hp")
character_schema = CharacterSchema()
multiple_character_schema = CharacterSchema(many=True)

# Endpoints
#   Add Endpoint
@app.route("/character/add", methods=["POST"])
def add_character():
    if request.content_type != "application/json":
        return jsonify("Error: Please send as JSON")
    
    post_data = request.get_json()
    pname = post_data.get("pname")
    cname = post_data.get("cname")
    pclass = post_data.get("pclass")
    race = post_data.get("race")
    height = post_data.get("height")
    weight = post_data.get("weight")
    gender = post_data.get("gender")
    age = post_data.get("age")
    size = post_data.get("size")
    basespeed = post_data("basespeed")
    level = post_data.get("level")
    alignment = post_data.get("alignment")
    description = post_data.get("description")
    biography = post_data.get("biography")
    copper = post_data.get("copper")
    silver = post_data.get("silver")
    gold = post_data.get("gold")
    platinum = post_data.get("platinum")
    strength = post_data.get("strength")
    dexterity = post_data.get("dexterity")
    constitution = post_data.get("constitution")
    intelligence = post_data.get("intelligence")
    wisdom = post_data.get("wisdom")
    charisma = post_data.get("charisma")
    hp = post_data.get("hp")
        
    new_record = Character(pname, cname, pclass, race, height, weight, gender, age, size, basespeed, level, alignment, description, biography, copper, silver, gold, platinum, strength, dexterity, constitution, intelligence, wisdom, charisma, hp)
    db.session.add(new_record)
    db.session.commit()

    return jsonify(character_schema.dump(new_record))

#   Get All Endpoint

@app.route("/character/get", methods=["GET"])
def get_characters():
    characters = db.session.query(Character).all()
    return jsonify(multiple_character_schema.dump(characters))

#   Get By ID Endpoint

@app.route("/character/get/<id>", methods=["GET"])
def get_character_by_id(id):
    character = db.session.query(Character).filter(Character.id == id).first()
    return jsonify(character_schema.dump(character))

# Delete by ID Endpoint

@app.route("/character/delete/<id>", methods=["DELETE"])
def delete_character_by_id(id):
    deleted_character = db.session.query(Character).filter(Character.id == id).first()

    db.session.delete(deleted_character)
    db.session.commit()

    return jsonify(character_schema.dump(deleted_character))

# Update By ID endpoint

@app.route("/character/update/<id>", methods=["PUT"])
def update_character_by_id(id):
    if request.content_type != "application/json":
        return jsonify("Error: Please send as JSON")

    put_data = request.get_json()
    pname = put_data.get("pname")
    cname = put_data.get("cname")
    pclass = put_data.get("pclass")
    race = put_data.get("race")
    height = put_data.get("height")
    weight = put_data.get("weight")
    gender = put_data.get("gender")
    age = put_data.get("age")
    size = put_data.get("size")
    basespeed = put_data("basespeed")
    level = put_data.get("level")
    alignment = put_data.get("alignment")
    description = put_data.get("description")
    biography = put_data.get("biography")
    copper = put_data.get("copper")
    silver = put_data.get("silver")
    gold = put_data.get("gold")
    platinum = put_data.get("platinum")
    strength = put_data.get("strength")
    dexterity = put_data.get("dexterity")
    constitution = put_data.get("constitution")
    intelligence = put_data.get("intelligence")
    wisdom = put_data.get("wisdom")
    charisma = put_data.get("charisma")
    hp = put_data.get("hp")
    
    updated_character = db.session.query(Character).filter(Character.id == id).first()

    # print(updated_character)

    if pname != None:
        updated_character.pname = pname
    if cname != None:
        updated_character.cname = pname
    if pclass != None:
        updated_character.pclass = gender
    if race != None:
        updated_character.race = race
    if height != None:
        updated_character.height = height
    if weight != None:
        updated_character.weight = weight
    if gender != None:
        updated_character.gender = gender
    if age != None:
        updated_character.age = age
    if size != None:
        updated_character.size = size
    if basespeed != None:
        updated_character.basespeed = basespeed
    if level != None:
        updated_character.level = level
    if alignment != None:
        updated_character.alignment = alignment
    if description != None:
        updated_character.description = description
    if biography != None:
        updated_character.biography = biography
    if copper != None:
        updated_character.copper = copper
    if silver != None:
        updated_character.silver = silver
    if gold != None:
        updated_character.gold = gold
    if platinum != None:
        updated_character.platinum = platinum
    if strength != None:
        updated_character.strength = strength
    if dexterity != None:
        updated_character.dexterity = dexterity
    if constitution != None:
        updated_character.constitution = constitution
    if intelligence != None:
        updated_character.intelligence = intelligence
    if wisdom != None:
        updated_character.wisdom = wisdom
    if charisma != None:
        updated_character.charisma = charisma
    if hp != None:
        updated_character.hp = hp

    db.session.commit()

    return jsonify(character_schema.dump(updated_character))


if __name__ == "__main__":
    app.run(debug=True)