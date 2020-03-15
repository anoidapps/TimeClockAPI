from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from schemas.user_schema import UserSchema
from schemas.organization_schema import OrganizationSchema


app = Flask(__name__)
ma = Marshmallow(app)

# postgres://YourUserName:YourPassword@YourHost:5432/YourDatabase
# postgres://Chris:emma@192.168.1.100:5432/AnoidClock
databaseConnection = "postgresql+psycopg2://Chris:emma@192.168.1.100:5432/AnoidClock"
app.config['SQLALCHEMY_DATABASE_URI'] = databaseConnection
db = SQLAlchemy(app)

from models.user import User
from models.organization import Organization

db.create_all()
db.session.commit()


@app.route("/")
def server_info():
	return "API Home"


@app.route("/users/<int:user_id>")
def get_user(user_id):
	user = db.session.query(User).get(user_id)
	schema = UserSchema()
	result = schema.dump(user)
	return str(result)


@app.route("/organization/<int:org_id>")
def get_org(org_id):
	organization = db.session.query(Organization).get(org_id)
	schema = OrganizationSchema
	result = schema.dump(organization)
	return str(result)


@app.route("/test/")
def test():
	user = User(first_name="David", last_name="Hileman", email="Dhileman@anoidapps.com")
	organization = Organization(name="AnoidApps")
	db.session.add(user)
	db.session.commit()

	db.session.add(organization)
	db.session.commit()
	return str(user) + "\n\n" + str(organization)


