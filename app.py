from flask import Flask
from flask_restful import Api,Resource,reqparse
from dbmodule import *

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class UserAll(Resource):
    def get(self):
        return get_all_jenis(),200

class User(Resource):
    def get(self,name):
        for user in users:
            if(name==user["name"]):
                return user,200
        return "User not found",404

api.add_resource(UserAll,"/api/users")
api.add_resource(User, "/api/user/<string:name>")
app.run(debug=True)