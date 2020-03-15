import datetime as dt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from Server import db


class User(db.Model):

	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password_hash = db.Column(db.Integer, unique=False)
	salt = db.Column(db.Integer, unique=False)

	admin = db.Column(db.Boolean(120), unique=False)

	# Foreign Key
	org_id = db.Column(db.Integer, unique=False)

	first_name = db.Column(db.String(80), unique=False)
	last_name = db.Column(db.String(80), unique=False)
	email = db.Column(db.String(120), unique=True)
	phone = db.Column(db.String(120), unique=False)

	# Constructor
	def __init__(self, first_name, last_name, email):
		self.user_id = None
		self.user_name = None
		self.password_hash = None
		self.salt = None

		self.org_id = None
		self.admin = False

		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone = None
		self.created_at = dt.datetime.now()

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

	# ????
	def __repr__(self):
		return "<User(name={self.first_name!r})>".format(self=self)

