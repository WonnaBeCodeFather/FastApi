from enum import Enum
from typing import Optional, List
from pydantic import BaseModel

from DIXI.review.schemas import Review


class ProductGender(str, Enum):
    male = 'male'
    female = 'female'


class ProductSeason(str, Enum):
    demi = 'demi'
    summer = 'summer'
    winter = 'winter'


class PriceCreate(BaseModel):
    price: float
    discount: Optional[int] = 0

    class Config:
        orm_mode = True


class PriceUpdate(PriceCreate):
    price: Optional[float]


class PriceUpdateResponse(PriceCreate):
    new_price: float


class Price(PriceUpdateResponse):
    id: int


class ProductUpdate(BaseModel):
    title: Optional[str]
    gender: Optional[ProductGender]
    season: Optional[ProductSeason]
    factory: Optional[str] = "DIXI"

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    title: str
    gender: ProductGender
    season: ProductSeason
    factory: str = "DIXI"
    price: PriceCreate

    class Config:
        orm_mode = True


class Product(ProductCreate):
    id: int
    price: Price


class ProductDetail(Product):
    review: List[Review]


