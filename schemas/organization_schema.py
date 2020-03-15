from marshmallow import Schema, fields, post_load


class OrganizationSchema(Schema):
	org_id = fields.Int()
	name = fields.Str()
	created_at = fields.DateTime()

	@post_load
	def make_org(self, data, **kwargs):
		from models.organization import Organization
		return Organization(**data)
