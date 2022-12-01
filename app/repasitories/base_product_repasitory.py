from typing import List
import uuid
from app.models.product import ProductIn, ProductOut, ProductStorage


class BaseProductRepasitory:
    
    def get_dy_id(self, id :uuid.UUID | int) -> ProductOut:
        raise NotImplementedError
    
    def get_all(self, limit :int, skip :int) -> List[ProductOut]:
        raise NotImplementedError
    
    def create(self, product :ProductIn) -> ProductOut:
        raise NotImplementedError
    
    def delete(self, id :uuid.UUID | int) -> ProductOut:
        raise NotImplementedError
    
    def put(self, id :uuid.UUID | int, product :ProductStorage) -> ProductOut:
        raise NotImplementedError