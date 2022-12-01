import datetime
import uuid
from app.models.product import ProductIn, ProductOut, ProductStorage


def conevrt_product_storege_to_out(product :ProductStorage) -> ProductOut:
    tmp_dict :dict = product.dict()
    tmp_dict.pop("secret_tocen", None)
    return ProductOut(**tmp_dict)


def convert_product_in_to_storege(product :ProductIn) -> ProductStorage:
    tmp_dict :dict = product.dict()
    product_storege = ProductStorage(id=uuid.uuid4(), created_at=datetime.datetime.now(), **tmp_dict)
    return product_storege