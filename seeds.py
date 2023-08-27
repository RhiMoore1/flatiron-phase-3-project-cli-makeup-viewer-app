from models import User, Makeup, user_makeup_favorite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///makeup_data.db')

Session = sessionmaker(bind=engine)
session = Session()

from faker import Faker
fake = Faker()



# Use faker to seed 5 Users
for __ in range(5):
    
    user_first_name = fake.first_name_female()
    user_last_name = fake.last_name()
    user_full_name = user_first_name + user_last_name
    
    new_user = User(
        username = user_full_name,
    )
 
    session.add(new_user)
    session.commit()