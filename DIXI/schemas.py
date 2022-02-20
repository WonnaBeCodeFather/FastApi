from enum import Enum

from pydantic import BaseModel
from typing import List


class ProductGender(str, Enum):
    male = 'male'
    female = 'female'


class ProductSeason(str, Enum):
    demi = 'demi'
    summer = 'summer'
    winter = 'winter'


class ReviewBase(BaseModel):
    username: str
    text: str

    class Config:
        orm_mode = True


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int


class PriceBase(BaseModel):
    price: float
    discount: int
    new_price: float

    class Config:
        orm_mode = True


class CreatePrice(BaseModel):
    price: float
    discount: int


class Price(PriceBase):
    id: int


class ProductBase(BaseModel):
    title: str
    gender: str
    season: str
    factory: str

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    gender: ProductGender
    season: ProductSeason
    price: List[CreatePrice]


class Product(ProductBase):
    id: int
    price: List[PriceBase]
    review: List[Review]
