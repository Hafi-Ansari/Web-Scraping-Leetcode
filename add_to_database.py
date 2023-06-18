from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv("MONGODB_CONNECTION_STRING")


# Create a MongoDB client
client = MongoClient(connection_string)

# Access a database
db = client["leetcode-questions"]

# Access a collection
collection = db["demo"]


dummy_data = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

# Insert the dummy data into the collection
insert_result = collection.insert_one(dummy_data)

# Check if the document was inserted successfully
if insert_result.inserted_id:
    print("Document inserted successfully.")
else:
    print("Failed to insert document.")

# Close the MongoDB connection
client.close()