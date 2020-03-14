from marshmallow import Schema, fields


class OrganizationSchema(Schema):
	org_id = fields.Int()
	name = fields.Str()
	created_at = fields.DateTime()
