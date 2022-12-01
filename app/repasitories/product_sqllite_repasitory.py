from typing import List, Dict, Optional
import uuid
from app.models.product import ProductIn, ProductOut, ProductStorage
from app.until.repasitory_untils import conevrt_product_storege_to_out, convert_product_in_to_storege
from app.repasitories.base_product_repasitory import BaseProductRepasitory