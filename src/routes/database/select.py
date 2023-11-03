from pymongo import MongoClient
from pymongo.cursor import Cursor
from bson import json_util

from routes.database.config import MONGO_URL
from routes.database.config import MONGO_DB
from routes.database.config import MONGO_COLLECTION

def get_from_db(search_data):
    try:
        client = MongoClient(MONGO_URL) 
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]

        result = collection.find(search_data)
        if isinstance(result, Cursor):
            result_json = json_util.dumps(result) 
            result_list = json_util.loads(result_json) 
            return result_list
        else:
            return False
    
    except Exception as e:
        print(f"Error from MongoDB: {str(e)}")
        return False
    
def get_from_ids(ids):
    try:
        client = MongoClient(MONGO_URL) 
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]

        result = collection.find({'id': {'$in': ids}})
        if isinstance(result, Cursor):
            result_json = json_util.dumps(result) 
            result_list = json_util.loads(result_json) 
            return result_list
        else:
            return False
    
    except Exception as e:
        print(f"Error from MongoDB: {str(e)}")
        return False            


