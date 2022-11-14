
import datetime
import json
from bson import json_util, ObjectId
from bson.json_util import dumps
from flask import jsonify, request
from flask_bcrypt import Bcrypt

from controllers.ErrorController import not_found
from database.Connection import Connection

class MovieController:
  def createMovie():
    if request.method == 'POST':
      data = request.json
      data['createdAt'] = datetime.datetime.utcnow()
      data['updatedAt'] = datetime.datetime.utcnow()
      Connection.db().movies.insert_one(data)
      resp = json.loads(json_util.dumps(data))
      return {
        'message': "Movie added successfully!",
        'data': [resp]
      }

  def getALlMovies():
    movies = Connection.db().movies.find()
    resp = dumps(movies)
    return resp

  def getMovieByID(movieID):
      movie = Connection.db().movies.find_one({'_id': ObjectId(movieID)})
      resp = dumps(movie)
      if (resp == 'null'):
        return not_found(movieID)
      else:
        return resp

  def updateMovieByID(movieID):
    data = request.json
    data['updatedAt'] = datetime.datetime.utcnow()
    checkMovie = Connection.db().movies.update_one({'_id': ObjectId(movieID)}, {'$set': data})
    if (checkMovie.modified_count == 0):
      return not_found(movieID)
    else:
      resp = json.loads(json_util.dumps(data))
      return {
        'message': "Movie updated successfully!",
        'data': [resp]
      }

  def delteMovieByID(movieID):
    checkMovie = Connection.db().movies.delete_one({'_id': ObjectId(movieID)})
    if (checkMovie.deleted_count == 0):
        return not_found(movieID)
    else:
      resp = jsonify("Movie deleted successfully!")
      resp.status_code = 200
      return resp