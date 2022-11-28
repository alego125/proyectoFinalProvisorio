from app.db.database import Base
# Importamos los tipode  datos a usar en sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship


class OrderReviews(Base):
    pass


class OrderPayments(Base):
    pass


class ProducCategory(Base):
    pass


class Sellers(Base):
    pass


class Products(Base):
    pass


class Orders(Base):
    pass


class OrderItems(Base):
    pass


class customer(Base):
    pass


class geolocation(Base):
    pass

