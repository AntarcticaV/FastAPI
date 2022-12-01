from typing import List
import uuid
from fastapi import APIRouter, Depends
from app.dependencies import get_product_repo
from app.models.product import ProductIn, ProductOut, ProductStorage
from app.repasitories.product import BaseProductRepasitory


router = APIRouter()

@router.get("/products", response_model = List[ProductOut])
async def get_products(products_repo :BaseProductRepasitory = Depends(get_product_repo), limit :int = 100, skip :int = 0):
    return products_repo.get_all(limit=limit, skip=skip)


@router.get("/product", response_model= ProductOut)
async def get_product(id :uuid.UUID, product_repo : BaseProductRepasitory = Depends(get_product_repo)):
    return product_repo.get_dy_id(id)


@router.post("/product", response_model= ProductOut)
async def create_product(product_in :ProductIn, product_repo :BaseProductRepasitory = Depends(get_product_repo)):
    return product_repo.create(product_in)


@router.delete("/delete", response_model= ProductOut)
async def delete_product(id :uuid.UUID, product_repo :BaseProductRepasitory = Depends(get_product_repo)):
    return product_repo.delete(id)


@router.put("/update", response_model= ProductOut)
async def put_product(id :uuid.UUID, product :ProductStorage, product_repo :BaseProductRepasitory = Depends(get_product_repo)):
    return product_repo.put(id, product)