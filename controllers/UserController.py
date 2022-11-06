
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient
from config import DATABASENAME, MONGO_URI, USER_COLLECTION
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

from controllers.ErrorController import not_found

client = MongoClient(MONGO_URI)
db = client[DATABASENAME]
collection = db[USER_COLLECTION]

def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    # validate the received values
    if _name and _email and _password and request.method == 'POST':
        
        # do not save password as a plain text
        _hashed_password = generate_password_hash(_password)
    
        # save details
        id = db.users._insert_one({'name': _name, 'email': _email, 'pwd': _hashed_password})
        resp = jsonify("User added successfully!")
        resp.status_code = 200
        return resp
    # else:
    #     return not_found()

def getALlUsers():
  users = db.users.find()
  resp = dumps(users)
  return resp

def getUserByID(userID):
    user = db.users.find_one({'_id': ObjectId(userID)})
    resp = dumps(user)
    if (resp == 'null'):
      return not_found(userID)
    else:
      return resp

def delete_user(id):
  db.users.delete_one({'_id': ObjectId(id)})
  resp = jsonify("User deleted successfully!")
  resp.status_code = 200
  return resp

def update_user():
  _id = request.json['_id']
  _name = request.json['name']
  _email = request.json['email']
  _password = request.json['pwd']

  # validate the received values
  if _name and _email and _password and _id and request.method == 'PUT':
      # do not save password as a plain text
      _hashed_password = generate_password_hash(_password)
  
      # save edits
      db.users.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': _name, 'email': _email, 'pwd': _hashed_password}})
      resp = jsonify("User updated successfully!")
      resp.status_code = 200
      return resp
  # else:
  #     return not_found()
