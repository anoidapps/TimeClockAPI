import datetime as dt


class Organization:

	# Constructor
	def __init__(self, org_id, name):
		self.org_id = org_id
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
