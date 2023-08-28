# flatiron-phase-3-project-cli-makeup-viewer-app

# Makeup Viewer App
### Description: 
The Makeup Viewer App is a CLI application that allows a user to create an account and view makeup products from a makeup database. Products can be viewed by name, by product_type, or by a user's favorites list.  The user can also create a new product, delete an existing product and add a product to their favorites list. 

### Installation Instructions:

1. Create a directory to clone the project from github
 - Go to https://github.com/RhiMoore1/flatiron-phase-3-project-cli-makeup-viewer-app in github and clone to your directory
 - navigate to directory and open in VS Code

2. Create virtual environment - run
 - pipenv --python 3.8.13
 - pipenv shell
3. populate the database with seeds - run
 - python3 seeds.py
4. run the file to begin program
 - python3 cli.py

 
### How to use the Makeup Viewer App:
After running the python3 cli.py command, the user is prompted to either login, signup or exit the program.  After logging in or signing up, the user is brought to the main menu.  When choosing "View Makeups" options for view by name, product type, or favorites populate.  Other main menu options include: create a new product, delete an existing product, or add a product to a favorites list.  The Makeup Viewer App allows users to view a large number makeup products and keep track of favorite products.


 ### Contributions
 Makeup database populated by the makeup API from
 http://makeup-api.herokuapp.com/api/v1/products
 


 ### MIT License

Copyright (c) 2023 RhiMoore1

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
