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
    if user_id==1:
        user = User(name="David", email="david.hileman@anoidapps.com")
    elif user_id==2:
        user = User(name="Chris", email="Hileman624@anoidapps.com")
    else:
        user = User(name="Not found", email="not@found.com")

    # TODO Get the user from a database

    schema = UserSchema()
    result = schema.dump(user)
    return result