from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from models.user import User
from schemas.user_schema import UserSchema


app = Flask(__name__)
ma = Marshmallow(app)

# postgres://YourUserName:YourPassword@YourHost:5432/YourDatabase
# postgres://Chris:emma@192.168.1.100:5432/AnoidClock
databaseConnection = "postgres://Chris:emma@192.168.1.100:5432/AnoidClock"
app.config['SQLALCHEMY_DATABASE_URI'] = databaseConnection
db = SQLAlchemy(app)

db.create_all()
db.session.commit()


@app.route("/")
def server_info():
	return "API Home"


@app.route("/users/<int:user_id>")
def get_user(user_id):
	user = User(first_name="David", last_name="Hileman", email="Dhileman@anoidapps.com")
	schema = UserSchema()
	result = schema.dump(user)
	return str(result)


@app.route("/test/")
def test():
	user = User(first_name="David", last_name="Hileman", email="Dhileman@anoidapps.com")

