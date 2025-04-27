from typing import TypeVar, Generic, Type, List, Optional
from app import db

T = TypeVar('T') #Isso vai pegar a Entidade, dinâmicamente no caso.

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def get_by_id(self, id: int) -> Optional[T]:
        return self.model.query.get(id)

    def get_all(self) -> List[T]:
        return self.model.query.all()

    def create(self, entity: T) -> T:
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, entity: T) -> None:
        db.session.delete(entity)
        db.session.commit()

    def update(self) -> None:
        db.session.commit()