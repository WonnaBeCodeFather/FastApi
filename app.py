from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from DIXI import crud, models, schemas, db
from DIXI.db import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/product/create")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.create_product(db, product)
    return db_product


@app.post("/review/create/{product_id}")
def create_review(product_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    db_review = crud.create_review(db, review, product_id)
    return db_review


@app.get('/product/')
def product_list(db: Session = Depends(get_db)):
    return crud.get_product_list(db)