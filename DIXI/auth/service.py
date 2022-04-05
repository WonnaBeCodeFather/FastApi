from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import bcrypt
from jose import jwt, JWTError
from pydantic import ValidationError
from datetime import datetime, timedelta
from DIXI import settings
from DIXI.auth import schemas, models
from DIXI.db import Session, get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')


def get_current_user(token: str = Depends(oauth2_scheme)) -> schemas.UserPermission:
    return AuthService.validate_token(token)


def is_admin_permission(user: schemas.UserPermission = Depends(get_current_user)):
    if user.is_admin:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to access")


class AuthService:
    @classmethod
    def verify_password(cls, password: str, hashed_password: str) -> bool:
        return bcrypt.verify(password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> schemas.UserPermission:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={
                'WWW-Authenticate': 'Bearer'
            },
        )
        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET,
                algorithms=[settings.jwt_algorithm]

            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = schemas.UserPermission.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def create_token(cls, user: models.User) -> schemas.Token:
        user_data = schemas.UserPermission.from_orm(user)

        now = datetime.utcnow()
        payLoad = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expiration),
            'sub': str(user_data.id),
            'user': user_data.dict(),
        }
        token = jwt.encode(
            payLoad,
            settings.JWT_SECRET,
            algorithm=settings.jwt_algorithm,
        )
        return schemas.Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_user(self, user_data: schemas.UserCreate) -> schemas.Token:
        user = models.User(
            username=user_data.username,
            password_hash=self.hash_password(user_data.password)
        )
        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> schemas.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={
                'WWW-Authenticate': 'Bearer'
            },
        )

        user = (
            self.session.query(models.User).filter(models.User.username == username).first()
        )
        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)