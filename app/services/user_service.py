from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreateSchema
from app.models.user import User
from marshmallow import ValidationError

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def get_user_by_id(self, user_id):
        return self.repository.get_by_id(user_id)

    def get_user_by_username(self, username):
        return self.repository.get_by_username(username)

    def get_user_by_email(self, email):
        return self.repository.get_by_email(email)

    def get_all_users(self):
        return self.repository.get_all()

    def create_user(self, data):
        schema = UserCreateSchema()
        try:
            validated_data = schema.load(data)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        if self.repository.get_by_username(validated_data["username"]):
            return {"message": "Usuário já existe"}, 400

        if self.repository.get_by_email(validated_data["email"]):
            return {"message": "Email já em uso"}, 400

        user = User(
            id=None,
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            role=validated_data["role"]
        )

        return self.repository.create(user), 201

    def delete_user(self, user_id):
        user = self.repository.get_by_id(user_id)
        if not user:
            return {"message": "Usuário não encontrado"}, 404
        self.repository.delete(user)
        return {"message": "Usuário deletado com sucesso"}, 200
