from marshmallow import Schema, fields


class JobSchema(Schema):
	job_id = fields.Int()
	name = fields.Str()
	description = fields.Str()
	address = fields.Str()
	org_id = fields.Int()

	latitude = fields.Float()
	longitude = fields.Float()

	created_at = fields.DateTime()
	
	@post_load
	def make_job(self, data, **kwargs):
		from models.job import Job
		return Job(**data)
