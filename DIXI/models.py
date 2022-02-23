from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.orm import relationship

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    gender = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    season = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    factory = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    price = relationship('Price', back_populates='product')
    review = relationship('Review', back_populates='product')


class Price(Base):
    __tablename__ = 'price'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    discount = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    new_price = sqlalchemy.Column(sqlalchemy.Float, default=0)
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('product.id'), nullable=False, unique=True)
    product = relationship('Product', back_populates='price')


class Review(Base):
    __tablename__ = 'review'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    text = sqlalchemy.Column(sqlalchemy.String(500), nullable=False)
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates='review')


class User(Base):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    password_hash = sqlalchemy.Column(sqlalchemy.String, nullable=False)