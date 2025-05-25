from fastapi import FastAPI, HTTPException
from app.database import get_db_collection
from app.utils import is_duplicate

app = FastAPI()
db_collection = get_db_collection()

@app.post("/add-data/")
async def add_data(item: dict):
    if is_duplicate(db_collection, item):
        raise HTTPException(status_code=400, detail="Duplicate data found")
    
    db_collection.insert_one(item)
    return {"message": "Data added successfully"}
