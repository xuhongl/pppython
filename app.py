from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (replace with your MongoDB connection string)
client = MongoClient("mongodb://admin:password@ec2-44-211-94-215.compute-1.amazonaws.com:27017/")
# client = MongoClient("mongodb://localhost:27017/")
db = client.restaurants_reviews  # Database name
collection = db.restaurants_reviews      # Collection name

@app.route('/')
def home():
    return "Welcome to the Restaurant Reviews App!"

@app.route('/restaurants')
def get_restaurants():
    # Retrieve all documents from the "restaurants" collection
    restaurants = collection.find()
    # Convert MongoDB documents to a list of dictionaries
    result = []
    for restaurant in restaurants:
        # Exclude the MongoDB object ID from the output
        restaurant["_id"] = str(restaurant["_id"])
        result.append(restaurant)
    return jsonify(result)

if __name__ == '__main__':
    # app.run(debug=True)
     app.run(host='0.0.0.0', debug=True)
