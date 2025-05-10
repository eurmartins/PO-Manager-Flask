from marshmallow import Schema, fields, validate, ValidationError
from app import ma
from app.models.user import User, RoleEnum

#list
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    product_name =  fields.Str(required=True)
    description = fields.Str()
    product_price = fields.Float()

#Post
class ProductCreateSchema(Schema):
    product_name =  fields.Str(required=True)
    description = fields.Str(required=True)
    product_name = fields.Float(required=True)

#Put only
class ProductUpdateSchema(Schema):
    product_name = fields.Str()
    description = fields.Str()
    product_name = fields.Float()

class ProductSummarySchema(Schema):
    product_name = fields.Str()
    product_price = fields.Float()

