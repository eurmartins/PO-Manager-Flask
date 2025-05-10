from app import db
from enum import Enum
from sqlalchemy import Enum as PgEnum

class RoleEnum(Enum):
    CLIENTE = 0
    ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(PgEnum(RoleEnum), nullable=False)