from flask import Flask
from flask_cors import CORS
from datetime import *
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import hashlib
import os

from schemas.user_schema import UserSchema
from schemas.organization_schema import OrganizationSchema
from schemas.job_schema import JobSchema
from schemas.entry_schema import EntrySchema

app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)

# postgres://YourUserName:YourPassword@YourHost:5432/YourDatabase
# postgres://Chris:emma@192.168.1.100:5432/AnoidClock
databaseConnection = "postgresql+psycopg2://Chris:emma@74.136.154.216:5432/AnoidClock"
app.config['SQLALCHEMY_DATABASE_URI'] = databaseConnection
db = SQLAlchemy(app)

from models.user import User
from models.organization import Organization
from models.job import Job
from models.entry import Entry

db.create_all()
db.session.commit()


@app.route("/")
def server_info():
	return "API Home"


@app.route("/users")
def get_users():
	#get all users by org id
	org_id = request.args.get('org-id', default = 0, type = int)
	users = db.session.query(User).filter(User.org_id == org_id).all()
	schema = UserSchema()
	result = schema.dumps(users, many=True)
	return str(result)


@app.route("/users/<int:user_id>")
def get_user(user_id):
	user = db.session.query(User).get(user_id)
	schema = UserSchema()
	result = schema.dumps(user)
	return str(result)


@app.route("/users", methods=['POST'])
def create_user():
	schema = UserSchema()
	content = request.get_json()
	user = schema.load(content)

	#create salt and hash
	salt = os.urandom(32)
	password = user.getPassword()
	password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
	user.setSalt(salt)
	user.setPasswordHash(password_hash)

	db.session.add(user)
	db.session.flush()
	db.session.commit()
	schema = UserSchema()
	obj_result = schema.dumps(result)

	return obj_result


# Needs Testing
@app.route("/users/<int:user_id>", methods={'UPDATE'})
def update_user(user_id, user_name, org_id, admin, first_name, last_name, email, phone, break_length):
	user = db.session.query(User).get(user_id)
	schema = UserSchema()

	user.user_name = user_name
	user.org_id = org_id
	user.admin = admin
	user.first_name = first_name
	user.last_name = last_name
	user.email = email
	user.phone = phone
	user.break_length = break_length

	db.session.commit()
	result = schema.dumps(user)
	return str(result)


# Needs Testing
@app.route("/users/<int:user_id>", methods={'DELETE'})
def delete_user(user_id):
	user = db.session.query(User).get(user_id)
	schema = UserSchema()
	db.session.delete()
	db.session.commit()
	result = schema.dumps(user)
	return str(result) + " was removed"


@app.route("/organizations")
def get_organizations():
	organizations = db.session.query(Organization).all()
	schema = OrganizationSchema()
	result = schema.dumps(organizations, many=True)
	return str(result)


@app.route("/organizations/<int:org_id>")
def get_org(org_id):
	organization = db.session.query(Organization).get(org_id)
	schema = OrganizationSchema()
	result = schema.dumps(organization)
	return str(result)


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


@app.route("/jobs")
def get_jobs():
	#get all jobs by org id
	org_id = request.args.get('org-id', default = 0, type = int)
	jobs = db.session.query(Job).filter(Job.org_id == org_id).all()
	schema = JobSchema()
	result = schema.dumps(jobs, many=True)
	return str(result)


@app.route("/jobs/<int:job_id>")
def get_job(job_id):
	job = db.session.query(Job).get(job_id)
	schema = JobSchema()
	result = schema.dumps(job)
	return str(result)


@app.route("/jobs", methods=['POST'])
def create_job():
	schema = JobSchema()
	content = request.get_json()
	print("Create Job")
	print(content)
	result = schema.load(content)
	print(result)
	db.session.add(result)
	db.session.flush()
	db.session.commit()
	schema = JobSchema()
	obj_result = schema.dumps(result)

	return obj_result


@app.route("/entries")
def get_entries():
	#get all entries by user id
	user_id = request.args.get('user-id', default = 0, type = int)
	entries = db.session.query(Entry).filter(Entry.user_id == user_id).all()
	schema = EntrySchema()
	result = schema.dumps(entries, many=True)
	return str(result)


@app.route("/entries/<int:entry_id>")
def get_entry(entry_id):
	entry = db.session.query(Entry).get(entry_id)
	schema = EntrySchema()
	result = schema.dumps(entry)
	return str(result)


# Needs Testing
@app.route("/entries", methods=['POST'])
def create_entry():
	schema = EntrySchema()
	content = request.get_json()
	result = schema.load(content)
	db.session.add(result)
	db.session.flush()
	db.session.commit()
	schema = EntrySchema()
	obj_result = schema.dumps(result)

	return obj_result


@app.route("/test")
def test():
	user = User(first_name="David", last_name="Hileman", email="Dhileman@anoidapps.com")
	organization = Organization(name="AnoidApps")
	organization2 = Organization(name="TheHilemanHour")
	job = Job(name="TimeClockAPI_AnoidApps", org_id="1")
	entry = Entry(user_id="1", start_time=datetime.today(), end_time=datetime.today())
	db.session.add(user)
	db.session.commit()

	db.session.add(organization)
	db.session.commit()

	db.session.add(organization2)
	db.session.commit()

	db.session.add(job)
	db.session.commit()

	db.session.add(entry)
	db.session.commit()
	return str(user) + "\n\n" + str(organization) + "\n\n" + str(organization2) + "\n\n" + str(job) + "\n\n" + str(entry)


