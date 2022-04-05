from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy import desc

from DIXI.db import Session, get_session
from DIXI.product import schemas, models


class ProductService:
    @classmethod
    def get_new_price(cls, price: float, discount: int) -> float:
        if discount:
            new_price = price - (price * (discount / 100))
        else:
            new_price = 0
        return float("{0:.2f}".format(new_price))

    @classmethod
    def set_attribute_model(cls, data: dict, model) -> dict:
        for key, value in data.items():
            setattr(model, key, value)
        return data

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[schemas.Product]:
        return self.session.query(models.Product).order_by(desc(models.Product.id)).all()

    def get_detail(self, id: int) -> models.Product:
        operation = self.session.query(models.Product).filter(models.Product.id == id).first()
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    def create_product(self, data: schemas.ProductCreate) -> schemas.Product:
        product = models.Product(title=data.title,
                                 gender=data.gender,
                                 season=data.season,
                                 factory=data.factory)
        self.session.add(product)
        self.session.commit()

        return self.create_price(product=product, data=data)

    def create_price(self, product, data: schemas.ProductCreate = Depends(create_product)) -> schemas.Product:
        parser_price = dict(data.price)
        new_price = self.get_new_price(**parser_price)
        price = models.Price(**parser_price, product_id=product.id, new_price=new_price)
        self.session.add(price)
        self.session.commit()
        return schemas.Product.from_orm(product)

    def update_product(self, product_id: int, data: schemas.ProductUpdate) -> schemas.ProductUpdate:
        data = data.dict(exclude_none=True)
        product_model = self.get_detail(product_id)
        self.set_attribute_model(data, product_model)
        self.session.commit()
        return schemas.ProductUpdate.parse_obj(data)

    def update_price(self, product_id: int, data: schemas.PriceCreate) -> schemas.PriceUpdateResponse:
        price_model = self.session.query(models.Price).filter(models.Price.product_id == product_id).first()
        data = data.dict(exclude_none=True)
        data["new_price"] = self.get_new_price(price=data["price"], discount=data["discount"])
        self.set_attribute_model(data, price_model)
        self.session.commit()
        return schemas.PriceUpdateResponse.parse_obj(data)

    def destroy_product_with_price(self, product_id: int) -> None:
        self.session.query(models.Price).filter(models.Price.product_id == product_id).delete()
        self.session.query(models.Product).filter(models.Product.id == product_id).delete()
        self.session.commit()
        return
