import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class BaseProduct(BaseModel):
    
    name :str
    description :Optional[str] = None


class ProductIn(BaseProduct):
    
    secret_tocen :str


class ProductOut(BaseProduct):
    
    id :uuid.UUID
    created_at :datetime.datetime


class ProductStorage(BaseProduct):
    
    id :uuid.UUID
    created_at :datetime.datetime
    secret_tocen :str