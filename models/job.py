import datetime as dt
from Server import db


class Job (db.Model):

	job_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), unique=False)
	org_id = db.Column(db.Integer, unique=False)

	description = db.Column(db.String(200), unique=False)
	address = db.Column(db.String(200), unique=False)

	# Passing a Double into a Float, or a Float into a Double
	latitude = db.Column(db.Float, unique=False)
	longitude = db.Column(db.Float, unique=False)

	# Constructor
	def __init__(self, name, description, org_id):
		self.job_id = None
		self.name = name
		self.org_id = org_id
		self.created_at = dt.datetime.now()

		self.description = description
		self.address = None
		self.latitude = None
		self.longitude = None

	# Sets the Job ID:
	def __setJobID__(self, job_id):
		self.job_id = job_id

	# Returns the Job ID:
	def __getJobID__(self):
		return self.job_id

	# Sets the Name:
	def __setName__(self, name):
		self.name = name

	# Returns the Name:
	def __getName__(self):
		return self.name

	# Sets the Org ID:
	def __setOrgID__(self, org_id):
		self.org_id = org_id

	# Returns the Org ID:
	def __getOrgID__(self):
		return self.org_id

	# Sets the description:
	def __setDescription__(self, description):
		self.description = description

	# Returns the description:
	def __getDescription__(self):
		return self.description

	# Sets the Address:
	def __setAddress__(self, address):
		self.address = address

	# Returns the address:
	def __getAddress__(self):
		return self.address

	# Sets the latitude:
	def __setLatitude__(self, latitude):
		self.latitude = latitude

	# Returns the Longitude:
	def __getLatitude__(self):
		return self.latitude

	# Sets the Longitude:
	def __setLongitude__(self, longitude):
		self.longitude = longitude

	# Returns the Longitude:
	def __getLongitude__(self):
		return self.longitude




