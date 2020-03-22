from marshmallow import Schema, fields


class UserSchema(Schema):
	user_id = fields.Int()
	org_id = fields.Int()
	admin = fields.Bool()

	username = fields.Str()
	password = fields.Str()
	password_hash = fields.Str()
	salt = fields.Str()

	first_name = fields.Str()
	last_name = fields.Str()
	# Email -> STR
	email = fields.Str()
	phone = fields.Str()

	break_length = fields.Int()

	created_at = fields.DateTime()
