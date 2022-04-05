from fastapi import APIRouter, Depends

from DIXI.auth.schemas import UserPermission
from DIXI.auth.service import get_current_user
from DIXI.review.schemas import ReviewCreate
from DIXI.review.service import ReviewService

review_router = APIRouter(
    prefix="/review",
    tags=["reviews"]
)


@review_router.post('/{product_id}/create', response_model=ReviewCreate)
def create_review(review: ReviewCreate,
                  product_id: int,
                  user: UserPermission = Depends(get_current_user),
                  service: ReviewService = Depends()):
    return service.create_review(data=review, product_id=product_id, user=user)


@review_router.delete("/{id}/delete")
def destroy_review(review_id: int,
                   service: ReviewService = Depends(),
                   user: UserPermission = Depends(get_current_user)) -> None:
    return service.destroy_review(review_id, user)
