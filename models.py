from sqlalchemy import (Column, String, Integer, Column, Index, Table, ForeignKey)
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()





user_makeup_favorite = Table(
    "user_makeup_favorites",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("makeup_id", ForeignKey("makeups.id"), primary_key=True)
)





class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    makeups = relationship("Makeup", secondary=user_makeup_favorite, back_populates="users")


    def __repr__(self):
        return f"\n User ID: {self.id}: "\
            + f"Username {self.username} "






class Makeup(Base):
    __tablename__ = "makeups"
    Index('index_name', 'name')
    Index('index_brand', 'brand')
    Index('index_product_type', 'product_type')

    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand = Column(String)
    product_type = Column(String)

    users = relationship("User", secondary=user_makeup_favorite, back_populates="makeups")


    def __repr__(self):
        return f"\n Makeup ID: {self.id}: "\
            + f"Product Name: {self.name} "\
            + f"Product Brand: {self.brand} "\
            + f"Product Type: {self.product_type}"