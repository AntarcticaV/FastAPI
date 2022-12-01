from app.repasitories.product import ProductTmpRepasitory


TMP_REPASITORY = ProductTmpRepasitory()


def get_product_repo() -> ProductTmpRepasitory():
    return TMP_REPASITORY