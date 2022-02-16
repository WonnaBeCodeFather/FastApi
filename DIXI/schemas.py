from pydantic import BaseModel
from typing import List


class ReviewBase(BaseModel):
    username: str
    text: str


class ReviewCreate(ReviewBase):
    product_id: int
    pass


class Review(ReviewBase):
    id: int


class PriceBase(BaseModel):
    price: float
    discount: int
    new_price: float


class CreatePrice(PriceBase):
    product_id: int


class Pice(PriceBase):
    id: int


class ProductBase(BaseModel):
    title: str
    gender: str
    season: str
    factory: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    price: List[Pice]
    review: List[Review]
