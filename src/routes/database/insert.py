from pymongo import MongoClient

from routes.database.config import MONGO_URL
from routes.database.config import MONGO_DB
from routes.database.config import MONGO_COLLECTION

def save_to_db(person_data):
    try:
        client = MongoClient(MONGO_URL) 
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        
        result = collection.insert_one(person_data)
        if result.inserted_id:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error saving to MongoDB: {str(e)}")
        return False