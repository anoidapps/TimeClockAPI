import datetime as dt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from Server import db


class User(db.Model):

	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password_hash = db.Column(db.String, unique=False)
	salt = db.Column(db.String(32), unique=False)

	admin = db.Column(db.Boolean, unique=False)

	# Foreign Key
	org_id = db.Column(db.Integer, unique=False)

	first_name = db.Column(db.String(80), unique=False)
	last_name = db.Column(db.String(80), unique=False)
	email = db.Column(db.String(120), unique=True)
	phone = db.Column(db.String(120), unique=False)
	break_length = db.Column(db.Integer, unique=False)

	# Constructor
	def __init__(self, username, password, first_name, last_name, email, phone, admin, org_id):
		self.user_id = None
		self.username = username
		self.password = password
		self.password_hash = None
		self.salt = None

		self.org_id = org_id
		self.admin = admin

		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone = phone
		self.break_length = None

		self.created_at = dt.datetime.now()

	# # Testing Constructor
	# def __schemaInit__(self, admin, email, first_name, last_name, org_id, password, phone, username):
	# 	user = User(first_name, last_name, email)
	# 	user.__setUserName__(username)
	# 	user.__setPassword__(password)
	# 	user.__setOrgID__(org_id)
	# 	user.__setAdminStatus__(admin)
	# 	user.__setPhone__(phone)
	# 	return user

	# Sets the user's User ID:
	def __setUserID__(self, user_id):
		self.user_id = user_id

	# Returns the user's User ID:
	def __getUserID__(self):
		return self.user_id

	# Sets the user's Username:
	def __setUserName__(self, username):
		self.username = username

	# Returns the user's Username:
	def __getUserName__(self):
		return self.username

	# Sets the user's Password Hash:
	def __setPasswordHash__(self, password_hash):
		self.password_hash = password_hash

	# Returns the user's Password Hash:
	def __getPasswordHash__(self):
		return self.password_hash

	# Sets the user's Salt:
	def __setSalt__(self, salt):
		self.salt = salt

	# Returns the user's Salt:
	def __getSalt__(self):
		return self.salt

	# Sets the user's Org ID:
	def __setOrgID__(self, org_id):
		self.org_id = org_id

	# Returns the user's Org ID:
	def __getOrgID__(self):
		return self.org_id

	# Sets the user's User ID:
	def __setAdminStatus__(self, admin):
		self.admin = admin

	# Returns the user's User ID:
	def __getAdminStatus__(self):
		return self.admin

	# Sets the user's First Name:
	def __setFirstName__(self, first_name):
		self.first_name = first_name

	# Returns the user's First Name:
	def __getFirstName__(self):
		return self.first_name

	# Sets the user's Last Name:
	def __setLastName__(self, last_name):
		self.last_name = last_name

	# Returns the user's Last Name:
	def __getLastName__(self):
		return self.last_name

	# Sets the user's Phone Number (Default == Null) :
	def __setPhone__(self, phone):
		self.phone = phone

	# Returns the user's Phone Number:
	def __getPhone__(self):
		return self.phone

	# Sets the user's Email Address:
	def __setEmail__(self, email):
		self.email = email

	# Returns the user's Email Address:
	def __getEmail__(self):
		return self.email

	# Sets the user's Break Length Address:
	def __setBreakLength__(self, break_length):
		self.break_length = break_length

	# Returns the user's Break Length Address:
	def __getBreakLength__(self):
		return self.break_length

	# Sets the user's Password Hash:
	def __setPassword__(self, password):
		self.password = password

	# Returns the user's Password Hash:
	def __getPassword__(self):
		return self.password

	# ????
	def __repr__(self):
		return "<User(name={self.first_name!r})>".format(self=self)

