from models import User, Makeup, user_makeup_favorite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///makeup_data.db')

Session = sessionmaker(bind=engine)
session = Session()

import json 
import requests 
from faker import Faker
fake = Faker()
print("🌱 Seeding DB...")


# Reset DB
session.query(User).delete()
session.query(Makeup).delete()
session.query(user_makeup_favorite).delete()


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




# Use the Makeup DB to populate the makeup by sending a request then parse as json
request = requests.get(f'http://makeup-api.herokuapp.com/api/v1/products.json')
makeup_data = json.loads(request.text)


BRANDS = ['mistura', 'benefit', 'dr. hauschka', 'misa', 'nyx', 'butter london', 'dior', 
          'clinique', 'rejuva minerals', 'mineral fusion', "l'oreal", 'moov', 'piggy paint', 
          'e.l.f.', 'physicians formula', 'fenty', 'alva', "maia's mineral galaxy", 'colourpop', 
          'annabelle', 'zorah', 'boosh', 'lotus cosmetics usa', 'marcelle', 'dalish', 'revlon', 
          'china glaze', 'smashbox', 'salon perfect', 'maybelline', 'covergirl', 'orly', 
          'milani', 'almay', 'deciem', 'green people', 'cargo cosmetics', 'anna sui', 'nudus', 
          'pacifica', 'w3llpeople', 'penny lane organics', 'stila', 'sinful colours', "burt's bees", 
          'sante', 'zorah biocosmetiques', 'glossier', 'coastal classic creation', 'pure anada', 
          'essie', 'suncoat', "c'est moi", 'marienatie', 'iman', "sally b's skin yummies", 
          'wet n wild']

MAKEUP_API_SEARCH_URL_BASE = "http://makeup-api.herokuapp.com/api/v1/products.json?brand="

makeup_product_ids = set()
for brand in BRANDS:
    response = requests.get(MAKEUP_API_SEARCH_URL_BASE + brand)
    json_data = json.loads(response.text)
    for makeup_product in json_data:
        new_makeup_product = Makeup(
            name = makeup_product["name"],
            brand = makeup_product["brand"],
            product_type = makeup_product["product_type"]
        )

        session.add(new_makeup_product)
        session.commit()


print("✅ Done seeding!")