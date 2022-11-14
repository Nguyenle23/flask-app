from pymongo import MongoClient
from config import DATABASENAME, MONGO_URI, USER_COLLECTION

class Connection:  
  def db():
    client = MongoClient(MONGO_URI)
    db = client[DATABASENAME]
    return db
