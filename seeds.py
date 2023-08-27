from models import User, Makeup, user_makeup_favorite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///makeup_data.db')

Session = sessionmaker(bind=engine)
session = Session()