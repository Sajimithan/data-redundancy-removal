def is_duplicate(collection, new_item):
    # Assume 'content' field must be unique
    return collection.find_one({"content": new_item.get("content")}) is not None
