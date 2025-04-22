from app import db
from enum import Enum
from sqlalchemy import Enum as PgEnum

class RoleEnum(Enum):
    CLIENTE = "CLIENTE"
    ADMIN = "ADMIN"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(PgEnum(RoleEnum), nullable=False)

    def __init__(self, id, username, password, email, role):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.role = role
