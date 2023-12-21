from pymongo import MongoClient

connection = MongoClient("mongodb://localhost:27017")

db = connection.money_manager

collection = db["users"]