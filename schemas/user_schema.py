from marshmallow import Schema, fields


class UserSchema(Schema):
	user_id = fields.Int()
	org_id = fields.Int()
	admin = fields.Bool()

	user_name = fields.Str()
	password_hash = fields.Str()
	salt = fields.Str()

	first_name = fields.Str()
	last_name = fields.Str()
	email = fields.Email()
	phone = fields.Str()
	created_at = fields.DateTime()
