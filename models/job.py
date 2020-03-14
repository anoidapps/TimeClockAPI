import datetime as dt


class Job:

	# Constructor
	def __init__(self, job_id, name):
		self.job_id = job_id
		self.name = name
		self.created_at = dt.datetime.now()

		self.description = None
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




