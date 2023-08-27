# Phase 3 Python Command Line Project Notes

### Project Requirements

* A CLI application that solves a real-world problem and adheres to best practices.
* A database created and modified with SQLAlchemy ORM with 2+ related tables.
* A well-maintained virtual environment using Pipenv.
* Proper package structure in your application.
* Use of lists and dicts.


### Main idea: 

* A Makeup App, for users to view makeup products and save them favorites list.
* Users will look at a list of makeup products and add them to a list of favorites.
* Users can see 1 makeup product.
* Users can see their list favorite makeup products.
* Users can remove a makeup product from the list favorites.


### How I will use the concepts I recently learned to meet the project requirements

* Object Oriented Python 
* class for User with attributes
* class for makeup_product with attributes

#### Database tables
 * Table: User
    - id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
    - username/login: STRING NOT NULL UNIQUE

 * Table: Makeup_Product
    - id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
    - name: STRING NOT NULL
    - brand: STRING NOT NULL
    - product_type: STRING NOT NULL

 * Table: (many to many) User_makeup_product == List of favorite makeup_products
    - id: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENT
    - makeup_product_id: INTEGER NOT NULL (FK)
    - user_id who favorited it: INTEGER NOT NULL (FK)

 - Object relationship
    - User can have many makeup_products in favorites
    - Makeup_product can be added to favorites by many users
    - User to Makeup_product == many-to-many
    - with join table user_makeup_favorite

- CRUD
- Create
    - create a list a makeup_product favorites
- Read
    - Read All
        - Display all makeup_products by product_type
        - Display favorite makeup_products
    - Read 1
        - Display 1 makeup_product by name
- Update
    - update product
- Delete
    - Remove a makeup_product from the database

 - Use of Data Structures
    - Single Source of Truth
    - LIST: User could have a list of makeup_products as ID's 
        - Join table
    - LIST: User could have a list of makeup_products as name's
        - Join table
    - DICTIONARY: Makeup_product has a set of attributes and values

 - Most challenging
    - Deciding how the data works with the join table