from flask import Flask
from flask_cors import CORS

from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from schemas.user_schema import UserSchema
from schemas.organization_schema import OrganizationSchema


app = Flask(__name__)
CORS(app)
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


@app.route("/users")
def get_users():
	user = db.session.query(User).all()
	schema = UserSchema()
	result = schema.dumps(user, many=True)
	return str(result)


@app.route("/users/<int:user_id>")
def get_user(user_id):
	user = db.session.query(User).get(user_id)
	schema = UserSchema()
	result = schema.dumps(user)
	return str(result)


@app.route("/organizations")
def get_organizations():
	organization = db.session.query(Organization).all()
	schema = OrganizationSchema()
	result = schema.dumps(organization, many=True)
	return str(result)


@app.route("/organizations/<int:org_id>")
def get_org(org_id):
	organization = db.session.query(Organization).get(org_id)
	schema = OrganizationSchema()
	result = schema.dumps(organization)
	return str(result)


# Needs Testing
@app.route("/organizations", methods=['POST'])
def create_org():
	schema = OrganizationSchema()
	content = request.get_json()
	result = schema.load(content)
	db.session.add(result)
	db.session.flush()
	db.session.commit()
	schema = OrganizationSchema()
	obj_result = schema.dumps(result)

	return obj_result


@app.route("/test")
def test():
	user = User(first_name="David", last_name="Hileman", email="Dhileman@anoidapps.com")
	organization = Organization(name="AnoidApps")
	organization2 = Organization(name="TheHilemanHour")
	db.session.add(user)
	db.session.commit()

	db.session.add(organization)
	db.session.commit()

	db.session.add(organization2)
	db.session.commit()
	return str(user) + "\n\n" + str(organization) + "\n\n" + str(organization2)


