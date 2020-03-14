from marshmallow import Schema, fields


class JobSchema(Schema):
	job_id = fields.Int()
	name = fields.Str()
	description = fields.Str()
	address = fields.Str()

	latitude = fields.Float()
	longitude = fields.Float()

	created_at = fields.DateTime()
