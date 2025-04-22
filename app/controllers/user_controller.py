from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.schemas.user_schemas import UserSchema

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

class UserController:
    def __init__(self):
        self.service = UserService()
        self.user_schema = UserSchema()
        self.user_list_schema = UserSchema(many=True)

        user_bp.add_url_rule('/', view_func=self.get_all_users, methods=['GET'])
        user_bp.add_url_rule('/<int:user_id>', view_func=self.get_user_by_id, methods=['GET'])
        user_bp.add_url_rule('/', view_func=self.create_user, methods=['POST'])
        user_bp.add_url_rule('/<int:user_id>', view_func=self.delete_user, methods=['DELETE'])

    def get_all_users(self):
        users = self.service.get_all_users()
        return self.user_list_schema.dump(users), 200

    def get_user_by_id(self, user_id):
        user = self.service.get_user_by_id(user_id)
        if not user:
            return jsonify({"message": "Usuário não encontrado"}), 404
        return self.user_schema.dump(user), 200

    def create_user(self):
        data = request.get_json()
        return self.service.create_user(data)

    def delete_user(self, user_id):
        return self.service.delete_user(user_id)

user_controller = UserController()
