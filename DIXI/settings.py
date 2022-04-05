from sqlalchemy.orm import declarative_base

Base = declarative_base()

jwt_secret: str
jwt_algorithm: str = 'HS256'
jwt_expiration = 3600


JWT_SECRET = '1bRsNVARnC4Rq73D4u3VKv6hwAjeP9313IcK6vfgskQ'
