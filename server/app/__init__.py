from flask import Flask, Blueprint
from flask_restful import Api
from pymongo import MongoClient

money_blueprint = Blueprint('money_blueprint', __name__)

app = Flask(__name__)
api = Api(app)
client = MongoClient()

from app import routes