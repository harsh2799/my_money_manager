from app import api 
from app.resources import Home

api.add_resource(Home, '/', '/home')