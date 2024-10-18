from .database import collection, todo_collection
from .models import TodoModel
from bson.objectid import ObjectId
import json
import logging

async def get_all_items():
    items = []
    # async for item in collection.find():
    #     items.append(TodoModel(**item))
    items = await todo_collection.find().to_list(100)
    logging.debug(items)
    # for item in items:
    #     item["id"] = str(item["_id"])  #
    return items


async def get_item_by_id(id: str):
    item = await collection.find_one({"_id": ObjectId(id)})
    if item:
        return TodoModel(**item)


async def create_item(item_data: dict):
    item = await collection.insert_one(item_data)
    new_item = await collection.find_one({"_id": item.inserted_id})
    return new_item


async def update_item(id: str, data: dict):
    if len(data) < 1:
        return False
    item = await collection.find_one({"_id": ObjectId(id)})
    if item:
        updated_item = await collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return updated_item.modified_count > 0


async def delete_item(id: str):
    item = await collection.find_one({"_id": ObjectId(id)})
    if item:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
