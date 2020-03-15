import datetime as dt
from Server import db


class Organization (db.Model):

	org_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), unique=False)

	# Constructor
	def __init__(self, name):
		self.org_id = None
		self.name = name
		self.created_at = dt.datetime.now()

	# Sets the Org ID:
	def __setOrgID__(self, org_id):
		self.org_id = org_id

	# Returns the Org ID:
	def __getOrgID__(self):
		return self.org_id

	# Sets the Name:
	def __setName__(self, name):
		self.name = name

	# Returns the Name:
	def __getName__(self):
		return self.name
