from marshmallow import Schema, fields, validate, ValidationError
from app import ma
from app.models.user import User, RoleEnum

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password",)  # Não serializa a senha

    username = fields.String(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    role = fields.Function(lambda obj: obj.role.value if obj.role else None, 
                        deserialize=lambda value: RoleEnum(value))

class UserCreateSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    role = fields.Integer(required=True, validate=validate.OneOf([0, 1])) 
    password = fields.String(required=True, validate=validate.Length(min=6)) 

