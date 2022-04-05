from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int


class UserPermission(User):
    is_admin: bool


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'