from pymongo import MongoClient

client = MongoClient("mongodb+srv://bazingaaboi:bazinga123@project-money-manager.uz0zjby.mongodb.net/?retryWrites=true&w=majority")

db = client.money_manager

collection = db["users"]