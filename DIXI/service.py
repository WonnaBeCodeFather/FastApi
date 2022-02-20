from typing import List
from fastapi import status, HTTPException

from fastapi import Depends
from sqlalchemy.orm import Session

from DIXI import models, schemas
from DIXI.db import get_session


class ProductService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[models.Product]:
        return self.session.query(models.Product).all()

    def get_detail(self, id: int) -> models.Product:
        operation = self.session.query(models.Product).filter(models.Product.id == id).first()
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    def create_product(self, data: schemas.ProductCreate):
        product = models.Product(title=data.title,
                                 gender=data.gender,
                                 season=data.season,
                                 factory=data.factory)
        self.session.add(product)
        self.session.commit()

        return self.create_price(product_id=product.id, data=data)

    def create_price(self, product_id: int, data: schemas.ProductCreate):
        parser_price = dict(*data.price)
        if parser_price['discount']:
            new_price = parser_price['price'] - (parser_price['price'] * (parser_price['discount'] / 100))
        else:
            new_price = 0

        price = models.Price(price=parser_price['price'],
                             discount=parser_price['discount'],
                             new_price=new_price,
                             product_id=product_id)
        self.session.add(price)
        self.session.commit()
        return data


class ReviewService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_review(self, product_id: int, data: schemas.ReviewCreate):
        data = data.dict()
        data['product_id'] = product_id
        review = models.Review(**data)
        self.session.add(review)
        self.session.commit()
        return data