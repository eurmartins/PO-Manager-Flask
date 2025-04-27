from typing import Any, Dict, Tuple, Optional
from marshmallow import ValidationError

from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreateSchema
from app.models.user import User

class UserService:
    def __init__(self):
        self.repository = UserRepository()
        self.create_schema = UserCreateSchema()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.repository.get_by_id(user_id)

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.repository.get_by_username(username)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.repository.get_by_email(email)

    def get_all_users(self) -> list[User]:
        return self.repository.get_all()

    def create_user(self, data: dict) -> Tuple[Dict[str, Any], int]:
        try:
            validated_data = self.create_schema.load(data)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        if self.repository.get_by_username(validated_data["username"]):
            return {"message": "Usuário já existe"}, 400

        if self.repository.get_by_email(validated_data["email"]):
            return {"message": "Email já em uso"}, 400

        user = User(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            role=validated_data["role"]
        )

        created_user = self.repository.create(user)
        return {"message": "Usuário criado com sucesso", "user_id": created_user.id}, 201

    def delete_user(self, user_id: int) -> Tuple[Dict[str, str], int]:
        user = self.repository.get_by_id(user_id)
        if not user:
            return {"message": "Usuário não encontrado"}, 404

        self.repository.delete(user)
        return {"message": "Usuário deletado com sucesso"}, 200
