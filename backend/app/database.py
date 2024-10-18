from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv("mongodb://localhost:27017")  

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client['test']
collection = database.get_collection('todo')
todo_collection = database.get_collection('todo')

