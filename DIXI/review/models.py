import sqlalchemy
from sqlalchemy.orm import relationship
from DIXI.product.models import Product

from DIXI.settings import Base


class Review(Base):
    __tablename__ = 'review'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    text = sqlalchemy.Column(sqlalchemy.String(500), nullable=False)
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('product.id'), nullable=False)
    owner = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    product = relationship(Product, back_populates='review')
