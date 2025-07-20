import os
from dotenv import load_dotenv
load_dotenv()
from pymongo.mongo_client import MongoClient
# uri = "mongodb+srv://soishi570:5PQCXLKCzBOTdGtL@cluster0.raz3aee.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(os.getenv("MONGO_DB_URL"))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)    
