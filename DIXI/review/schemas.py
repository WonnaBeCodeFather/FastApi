from pydantic import BaseModel


class ReviewBase(BaseModel):
    username: str
    text: str

    class Config:
        orm_mode = True


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
