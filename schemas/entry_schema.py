from marshmallow import Schema, fields


class EntrySchema(Schema):
	entry_id = fields.Int()
	user_id = fields.Int()
	start_time = fields.DateTime()
	end_time = fields.DateTime()
	break_length = fields.Int()  # Minutes
	created_at = fields.DateTime()
