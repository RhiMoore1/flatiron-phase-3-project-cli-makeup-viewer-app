# Phase 3 Python CLI Project Notes - Configuring Virtual Environment

### Alembic Commands and Seeds Cheat Sheet
- [Notion Link](https://furry-shrimp-4f0.notion.site/Alembic-Commands-Cheat-Sheet-1561ad0f713d43bfbb3f559a3e29ec03?pvs=25)
- [Seeds Cheatsheet](https://furry-shrimp-4f0.notion.site/-DB-Seeds-Cheat-Sheet-for-SQLAlchemy-Alembic-CLI-fee13f02dd68491bb338aac2e9d4f41a)
- [Alembic Commands](https://furry-shrimp-4f0.notion.site/Alembic-Commands-and-DB-Query-Cheat-Sheet-1561ad0f713d43bfbb3f559a3e29ec03)


## 1. create virtual environment
   - python --version
   - pipenv --python 3.8.13
        - url source in pip file specifies the source the dependencies come from
        - dependencies come from pypi
        - environment created with python version 3.8.13

## 2. install dependencies
  - pipenv install sqlalchemy==1.4.41 alembic ipdb faker requests simple_term_menu prettycli
    - SQLAlchemy 1.4.41 (Python SQL toolkit and Object Relational Mapper)
    - Alembic (migration manager)
    - ipdb (Python debugger)
    - faker (to generate fake data)
    - simple_term_menu (menus for CLI)
    - prettycli (CLI flair)

## 3. create the migration environment
 - run pipenv shell to go into virtual environment
 - Initialize the migrations with Alembic, the migration management tool
    - alembic init migrations
    - generates an alembic.init file
    - generates a migrations folder
 - Configure Alembic to work with SqlAlchemy DB
    - in the alembic.ini file
        - specify the kind of SQL - line 63 - sqlalchemy.url=sqlite:///data.db
        - data.db is the name of the DB working with
    - in the migrations env.py file
        - lines 19 - 20
        - assign target_metadata the correct Base
        - Base is connected to each of our models 
        - the data about our models is saved and stored in metadata
        - compare differences between the database and schemas
        - line 19. from models import Base
        - line 20. target_metadata = Base.metadata
        - comment out line 21.
        - line 66. add ,render_as_batch=True
            - this allows for ALTER table support
    - create models.py file to define Base
        - import declarative_base from sqlalchemy.orm
        - create a variable to capture the return value of declarative_base()
        - which is the base class that the schemas will inherit from 
## 4. generate a migration 
 - alembic revision -m 'empty init'
    - generates a migration
    - has an upgrade and downgrade function
        - alembic upgrade head
        - alembic downgrade version

## 5. create schema (python classes or models)
 - in order for Alembic to autogenerate our tables
    - import the column, integer, string etc. in Models.py
    - create a class and table in Models.py
    - for table to be a schema, need to inherit from Base
    - create class attribute ID set to Column()
 - alembic revision --autogenerate -m 'create User table with primary key'
 - alembic upgrade head
 - the data.db is created
 - alembic downgrade -1 goes back one
 - alembic downgrade base goes back to original version
 - a migration version with timestamp and message is created


## 6. populate the database with seeds
 - create new file seeds.py
 - import User from models
 - create an engine
    - establish a connection from sqlalchemy to the database
    - pass in string that is the same that we added to alembic.init file data.db
 - create a session to speak to the database
    - create session object and bind the engine to it
    - instantiate it and capture the return object
 - create some users instances
    - create the sql necessary to add the users to the db session.bulk_save_objects(users)
    - execute the sql session.commit()
    - python3 seeds.py

## 7. populate data from an API
 - use requests to get data from the API
 - send a request
    - request = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={random.choice(letters)}")
 - take request and parse as json
    - y = json.loads(request.text)

## 8. test the relationship one-to-many 
 - one-to-many describes how one table relates to another
    - Owner : Pet (Owner has many Pets) (one Pet belongs to a single Owner)
    - add a new column to the table that belongs to the other table
        - Pet belongs to an Owner (add a Foreign Key of owner_id to the Pet table)
        - An owner_id is used to label the pet
    - PETS table
    - pass a FK object as an argument to a Column object
        - on the Pet table include: owner_id = Column(Integer, ForeignKey('owner.id'))
    - OWNERS table
    - create another class attribute -pets
    - a way to retrieve all Pet instances that are associated with a particular Owner
        - pets = relationship("Pet", backref="owner")
        - migrations/versions 
            - add to batch_op.create_foreign_key("user_pets")
            - add to batch_op.drop_constraint("user_pets")
        -  alembic upgrade head
    - can query through: owner.pets

## 9. test the relationship many-to-many   
 - many-to-many describes a relationship type between two tables
 - a Recipe has many Recipe Ingredients 
    - Recipe has many Ingredients through Recipe Ingredients
 - Ingredient has many Recipe Ingredients
    - Ingredient has many Recipes through Recipe Ingredients
 

 - Tables
    - User
        - a User has many makeup product favorites
    - Makeup
        - a Makup product can be favorited by many Users
    - User_Makeup_Favorites (JOIN)
        - PK   id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
        - FK2  user_id who favorited it: INTEGER NOT NULL (FK)
        - FK2  makeup_product_id: INTEGER NOT NULL (FK)
    - the JOIN table bridges the User and Makeup tables by capturing the two PK
        - establish the relationship in the coresponding tables
        - Makeup_products = relationship("Makeup", secondary=user_makeup_favorites)
        - Users = relationship("User", secondary=user_makeup_favorites)
        - 
    - session.query(Makeup).get(id)

## 10. create the entry point for CLI
 - create a new cli.py file
    - create a cli class and call start method to instantiate new cli and run start method
        - app = Cli()
        - app.start()

## 11. Git branches
 - git checkout -b migrations_work
    - Switched to a new branch 'migrations_work'
- git push origin migrations_work (after git add . and git commit -m' ')
- git checkout main 
    - Switched to branch 'main'
    - git merge migrations_work
    - git push
    - Your branch is up to date with 'origin/main'.

## Notes for API data
### For working with an API and retrieving json data
 - import requests
 - import json

### Example request
 - response = requests.get(API_URL)
 - json_data = json.loads(response.text)
