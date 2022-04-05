from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate, add_pagination

from DIXI.auth.schemas import UserPermission
from DIXI.auth.service import is_admin_permission
from DIXI.product.schemas import ProductCreate, Product, ProductDetail, ProductUpdate, PriceCreate, PriceUpdateResponse
from DIXI.product.service import ProductService

product_router = APIRouter(
    prefix="/product",
    tags=["product"]
)


@product_router.post("/create", response_model=Product, dependencies=[Depends(is_admin_permission)])
def create_product(product: ProductCreate,
                   service: ProductService = Depends()):
    return service.create_product(product)


@product_router.get('/', response_model=Page[Product])
def product_list(service: ProductService = Depends()):
    return paginate(service.get_list())


@product_router.get('/{product_id}', response_model=ProductDetail)
def product_detail(product_id: int, service: ProductService = Depends()):
    return service.get_detail(product_id)


@product_router.put('/{product_id}/update', response_model=ProductUpdate, dependencies=[Depends(is_admin_permission)])
def update_product(product_id: int, data: ProductUpdate,
                   service: ProductService = Depends()):
    return service.update_product(product_id, data)


@product_router.put("/{product_id}/price/update", response_model=PriceUpdateResponse,
                    dependencies=[Depends(is_admin_permission)])
def update_price(product_id: int, data: PriceCreate,
                 service: ProductService = Depends()):
    return service.update_price(product_id, data)


@product_router.delete("/{product_id}/delete", dependencies=[Depends(is_admin_permission)])
def destroy_product_with_price(product_id: int, service: ProductService = Depends()) -> None:
    return service.destroy_product_with_price(product_id)


add_pagination(product_router)
