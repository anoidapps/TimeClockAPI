from flask import Flask
from flask import request
from flask_marshmallow import Marshmallow
from models.user import User
from schemas.user_schema import UserSchema

app = Flask(__name__)
ma = Marshmallow(app)

@app.route("/")
def server_info():
    return "API Home"


@app.route("/users/<int:user_id>")
def getUser(user_id):
    # get a user by id
    user = User(name="David", email="david.hileman@anoidapps.com")
    schema = UserSchema()
    result = schema.dump(user)
    return result