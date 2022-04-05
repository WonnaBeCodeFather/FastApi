from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from DIXI.auth.schemas import Token, UserCreate, UserPermission, User
from DIXI.auth.service import AuthService, get_current_user

user_router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@user_router.post('/login', response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends()):
    return service.authenticate_user(
        form_data.username,
        form_data.password
    )


@user_router.post('/registration', response_model=Token)
def registration(user_data: UserCreate, service: AuthService = Depends()):
    return service.register_new_user(user_data)


@user_router.get('/self-user', response_model=UserPermission)
def get_user(user: User = Depends(get_current_user)):
    return user



