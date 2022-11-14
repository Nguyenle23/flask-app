
import datetime
import json
from bson import json_util, ObjectId
from bson.json_util import dumps
from flask import jsonify, request
from flask_bcrypt import Bcrypt

from controllers.ErrorController import not_found
from database.Connection import Connection

class UserController:
  def createUser():
    if request.method == 'POST':
      data = request.json
      
      data['avatar'] = ''
      data['createdAt'] = datetime.datetime.utcnow()
      data['updatedAt'] = datetime.datetime.utcnow()

      if (len(data['password']) <= 6):
        return jsonify('Password must be at least 6 characters long')
      else:
        data['password'] = Bcrypt().generate_password_hash(data['password']).decode('utf-8')
        checkEmailExist = Connection.db().users.find_one({'email': data.get('email')})
        if (checkEmailExist == None):
          Connection.db().users.insert_one(data)
          resp = json.loads(json_util.dumps(data))
          return {
            'message': "User added successfully!",
            'data': [resp]
          }
        else:
          resp = jsonify("User already exists!")
          resp.status_code = 409
          return resp

  def getALlUsers():
    users = Connection.db().users.find()
    resp = dumps(users)
    return resp

  def getUserByID(userID):
      user = Connection.db().users.find_one({'_id': ObjectId(userID)})
      resp = dumps(user)
      if (resp == 'null'):
        return not_found(userID)
      else:
        return resp

  def updateUserByID(userID):
    data = request.json
    data['updatedAt'] = datetime.datetime.utcnow()

    if (len(data['password']) <= 6):
      return jsonify('Password must be at least 6 characters long')
    else:
      data['password'] = Bcrypt().generate_password_hash(data['password']).decode('utf-8')
      checkUser = Connection.db().users.update_one({'_id': ObjectId(userID)}, {'$set': data})
      if (checkUser.modified_count == 0):
        return not_found(userID)
      else:
        resp = json.loads(json_util.dumps(data))
        return {
          'message': "User updated successfully!",
          'data': [resp]
        }

  def deleteUserByID(userID):
    checkUser = Connection.db().users.delete_one({'_id': ObjectId(userID)})
    if (checkUser.deleted_count == 0):
        return not_found(userID)
    else:
      resp = jsonify("User deleted successfully!")
      resp.status_code = 200
      return resp