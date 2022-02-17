from sqlalchemy.orm import Session
from DIXI import models, schemas


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(title=product.title, gender=product.gender, season=product.season,
                                factory=product.factory)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product_list(db: Session):
    return db.query(models.Product).all()


def create_review(db: Session, review: schemas.ReviewCreate, product_id: int):
    db_review = models.Review(username=review.username, text=review.text, product_id=product_id)

    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review