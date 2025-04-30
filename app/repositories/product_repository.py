from typing import Optional
from app.models.product import Product
from app.repositories.base_repository import BaseRepository

class ProductRepository(BaseRepository[Product]):

    def __init__(self):
        super().__init__(Product)

    def get_by_product_name(self, product_name: str) -> Optional[Product]:
        return self.model.query.filter_by(product_name=product_name).first()