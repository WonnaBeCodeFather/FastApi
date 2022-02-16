from sqlalchemy.orm import Session
from DIXI import models, schemas


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(title=product.title, gender=product.gender, season=product.season,
                                factory=product.factory, discount=product.discount, new_price=product.new_price)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


