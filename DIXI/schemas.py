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


class ProductUpdate(BaseModel):
    title: str
    gender: str
    season: str
    factory: str

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    id: int
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
    price: List[PriceBase]
    review: List[Review]


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

