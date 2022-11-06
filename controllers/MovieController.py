
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient
from config import DATABASENAME, MONGO_URI, USER_COLLECTION

from controllers.ErrorController import not_found

client = MongoClient(MONGO_URI)
db = client[DATABASENAME]
collection = db[USER_COLLECTION]


def getALlMovies():
  movies = db.movies.find()
  resp = dumps(movies)
  return resp

def getMovieByID(movieID):
    movie = db.movies.find_one({'_id': ObjectId(movieID)})
    resp = dumps(movie)
    if (resp == 'null'):
      return not_found(movieID)
    else:
      return resp
