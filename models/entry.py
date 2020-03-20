import datetime as dt
from Server import db


# Constructor
class Entry (db.Model):

	entry_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, unique=False)

	start_time = db.Column(db.DateTime, unique=False)
	end_time = db.Column(db.DateTime, unique=False)
	break_length = db.Column(db.Integer, unique=False)

	def __init__(self, user_id, start_time, end_time):
		self.entry_id = None
		self.user_id = user_id

		self.start_time = start_time
		self.end_time = end_time
		self.break_length = None

		self.created_at = dt.datetime.now()

	# Sets the Entry ID:
	def __setEntryID__(self, entry_id):
		self.entry_id = entry_id

	# Returns the Entry ID:
	def __getEntryID__(self):
		return self.entry_id

	# Sets the User ID:
	def __setUserID__(self, user_id):
		self.user_id = user_id

	# Returns the User ID:
	def __getUserID__(self):
		return self.user_id

	# Sets the Start Time:
	def __setStartTime__(self, start_time):
		self.start_time = start_time

	# Returns the Start Time:
	def __getStartTime__(self):
		return self.start_time

	# Sets the End Time:
	def __setEndTime__(self, end_time):
		self.end_time = end_time

	# Returns the End Time:
	def __getEndTime__(self):
		return self.end_time

	# Sets the BreakLength:
	def __setBreakLength__(self, break_length):
		self.break_length = break_length
	
	# Returns the BreakLength:
	def __getBreakLength__(self):
		return self.break_length
