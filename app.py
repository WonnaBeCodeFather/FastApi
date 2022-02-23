from typing import List

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from DIXI import models, schemas, db
from DIXI.db import Session
from DIXI import service
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.post("/product/create")
def create_product(product: schemas.ProductCreate, service: service.ProductService = Depends()):
    return service.create_product(product)


@app.get('/product/', response_model=List[schemas.ProductBase])
def product_list(service: service.ProductService = Depends()):
    return service.get_list()


@app.get('/product/{id}/', response_model=schemas.Product)
def product_detail(id: int, service: service.ProductService = Depends()):
    return service.get_detail(id)


@app.get('/tester')
def test(service: service.ProductService = Depends()):
    return service.test()


@app.post('/product/{product_id}/review', response_model=schemas.ReviewCreate)
def create_review(review: schemas.ReviewCreate, product_id: int, service: service.ReviewService = Depends()):
    return service.create_review(data=review, product_id=product_id)


@app.put('/product/{id}/', response_model=schemas.ProductUpdate)
def update_product(id: int, data: schemas.ProductUpdate, service: service.ProductService = Depends()):
    return service.update_product(id, data)


@app.post('/login', response_model=schemas.Token)
def login(data: OAuth2PasswordRequestForm = Depends()):
    pass


@app.post('/registration', response_model=schemas.Token)
def registration(data: schemas.UserCreate):
    pass
