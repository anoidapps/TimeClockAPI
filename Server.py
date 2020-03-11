from flask import Flask
from flask import request

app = Flask(__name__)

cache = {}


@app.route("/")
def server_info():
    return "Webserver home"


@app.route("/users/<int:user_id>")
def getUser(user_id):
    # get a user by id
    return "{\"user_id\":1,\"name\":\"David\",\"position\":\"Developer\"}"

