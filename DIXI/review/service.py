from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import Session

from DIXI.auth.schemas import UserPermission
from DIXI.auth.service import get_current_user
from DIXI.review import models, schemas
from DIXI.db import get_session


class ReviewService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_review(self, product_id: int, data: schemas.ReviewCreate,
                      user: UserPermission = Depends(get_current_user)) -> schemas.ReviewCreate:
        data = data.dict()
        data['product_id'] = product_id
        review = models.Review(**data, owner=user.id)
        self.session.add(review)
        self.session.commit()
        return schemas.ReviewCreate.from_orm(review)

    def destroy_review(self, review_id, user: UserPermission) -> None:
        review = self.session.query(models.Review).filter(models.Review.id == review_id).first()
        if user.id == review.owner or user.is_admin:
            review.delete()
        else:
            return
