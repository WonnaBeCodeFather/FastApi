import sqlalchemy
from sqlalchemy.orm import relationship, backref

from DIXI.settings import Base


class Product(Base):
    __tablename__ = 'product'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    gender = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    season = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    factory = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    # price = relationship('Price', useList=False,  back_populates='product')
    review = relationship('Review', back_populates='product')


class Price(Base):
    __tablename__ = 'price'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    discount = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    new_price = sqlalchemy.Column(sqlalchemy.Float, default=0)
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('product.id'), nullable=False, unique=True)
    product = relationship('Product', backref=backref("price", uselist=False))
