from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_collection():
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client["redundancy_system"]
    return db["data_entries"]
