from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json 

load_dotenv()
connection_string = os.getenv("MONGODB_CONNECTION_STRING")


# Create a MongoDB client
client = MongoClient(connection_string)

# Access a database
db = client["leetcode-questions"]

# Access a collection
collection = db["demo"]


# Read the JSON file
with open("questions.json") as json_file:
    data = json.load(json_file)

# Insert the JSON objects into the collection
collection.insert_many(data)

# Close the MongoDB connection
client.close()
