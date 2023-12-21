from flask import Flask, Blueprint
from flask_restful import Api

money_blueprint = Blueprint('money_blueprint', __name__)

app = Flask(__name__)
api = Api(app)

from app import routes