from app.models.user import User
from app import db

class UserRepository:
    
    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_all(self):
        return User.query.all()

    def create(self, user):
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()

    def update(self):
        db.session.commit()
