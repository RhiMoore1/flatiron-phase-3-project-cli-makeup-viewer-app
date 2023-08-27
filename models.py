from sqlalchemy import (Column, String, Integer, Column, Index)
from sqlalchemy.orm import declarative_base
Base = declarative_base()




class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)





class Makeup(Base):
    __tablename__ = "makeups"
    Index('index_name', 'name')
    Index('index_brand', 'brand')
    Index('index_product_type', 'product_type')

    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand = Column(String)
    product_type = Column(String)