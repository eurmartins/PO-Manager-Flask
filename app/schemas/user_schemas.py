from marshmallow import Schema, fields, validate, validates, ValidationError
from app import ma
from app.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password",)

    username = fields.String(required = True, validate = validate.Length(min = 3, max = 50))
    email = fields.Email(required = True)
    role = fields.String(validate =  validate.OneOf(["CLIENTE", "ADMIN"]))

class UserCreateSchema(UserSchema):
    password = fields.String(required = True, load_only = True, validate = validate.Length(min = 6))