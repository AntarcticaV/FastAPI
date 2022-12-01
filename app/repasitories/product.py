from typing import List, Dict, Optional
import uuid
from app.models.product import ProductIn, ProductOut, ProductStorage
from app.until.repasitory_untils import conevrt_product_storege_to_out, convert_product_in_to_storege
from app.repasitories.base_product_repasitory import BaseProductRepasitory


class ProductTmpRepasitory(BaseProductRepasitory):
    
    def __init__(self,):
        self._dict_products :Dict[uuid.UUID, ProductStorage] = {}
    
    def get_dy_id(self, id: uuid.UUID) -> Optional[ProductOut]:
        product :ProductStorage = self._dict_products.get(id, None)
        if product is None:
            return None
        product_out :ProductOut = conevrt_product_storege_to_out(product)
        return product_out
    
    def get_all(self, limit: int, skip: int) -> List[ProductOut]:
        product_out_list :List[ProductOut] = []
        for _, product in self._dict_products.items():
            product_out_list.append(conevrt_product_storege_to_out(product))
        return product_out_list[skip:skip+limit]
    
    def create(self, product: ProductIn) -> ProductOut:
        product_storege :ProductStorage = convert_product_in_to_storege(product)
        self._dict_products.update({product_storege.id: product_storege})
        product_uot :ProductOut = conevrt_product_storege_to_out(product_storege)
        return product_uot
    
    def delete(self, id :uuid.UUID) -> ProductOut:
        product :ProductStorage = self._dict_products.get(id, None)
        if product is None:
            return None
        self._dict_products.pop(id)
        return conevrt_product_storege_to_out(product)
    
    def put(self, id : uuid.UUID, product: ProductStorage) -> ProductOut:
        self._dict_products.update({id: product})
        product_in_dict :ProductStorage = self._dict_products.get(id, None)
        if product is None:
            return None
        return conevrt_product_storege_to_out(product_in_dict)