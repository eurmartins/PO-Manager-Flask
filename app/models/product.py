from app import db
from enum import Enum
from sqlalchemy import Enum as PgEnum

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=True)
    product_price = db.Column(db.Float, unique=True, nullable=True)
