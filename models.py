from sqlalchemy import (Column, String, Integer, Column)
from sqlalchemy.orm import declarative_base
Base = declarative_base()




class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)