from simple_term_menu import TerminalMenu
from sqlalchemy import create_engine
import time, os
from models import User, Makeup
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

engine = create_engine('sqlite:///makeup_data.db')
Session = sessionmaker(bind=engine)
session = Session()

class Cli():
    def __init__(self):
        self.current_user = None
        self.current_makeup = None
        self.current_makeup_product = None

    # START PROGRAM
    def start(self):
        self.clear_display()
        options = ["Login", "Sign Up", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if options[menu_index] == "Login":
            self.handle_login()
        elif options[menu_index] == "Sign Up":
            self.handle_signup()
        else:
            self.handle_exit()


    # LOGIN
    def handle_login(self):
        self.clear_display()
        username = input("Enter Username: ")
        
        user = User.find_by_username(username)
        if not user:
            print("User does not exist.")
            time.sleep(1)
            self.start()
            return
        else:
            self.current_user = user
            self.handle_manage_makeups()


    # SIGNUP
    def handle_signup(self):
        self.clear_display()
        username = input("Create a Username: ")

        if len(username) < 6:
            print('Username must be longer than 5 characters, please try again')
            time.sleep(3)
            self.handle_signup()
        else:
            user = User.find_by_username(username)
            if not user:
                user = User(username)
                session.add(user)
                self.current_user = user
                session.commit()
                print(f"Your Username is: {user.username}")
                time.sleep(3)
                self.handle_manage_makeups()
            else:
                print("User already exists. Please log in or create a new user.")
                time.sleep(3)
                self.start()
 

# MANAGE MAKEUP - ENTRY POINT 
    def handle_manage_makeups(self):
        # self.clear_display()
        options = ["View Makeups", "Create a Makeup", "Delete a Makeup", "Favorite a Makeup", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if menu_index == 0:
            print("View makeups")
            self.handle_view_makeups()    
        elif menu_index == 1:
            print("Create a makeup")
            self.handle_create_new_makeup()
        elif menu_index == 2:
            print("Delete a makeup")
            self.handle_delete_a_makeup()
        elif menu_index == 3:
            print("Favorite a makeup")
            self.current_makeup_product = input("Enter a makeup name: ")
            self.handle_favorite_a_makeup(self.current_user.id, self.current_makeup_product)
        else:
            self.handle_exit()


# VIEW MAKEUP - ENTRY POINT
    def handle_view_makeups(self):
        options = ["View by product name", "View by product type", "View favorites", "Main Menu", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_index = terminal_menu.show()

        if menu_index == 0:   
            user_input_makeup_name = input("View by name or type 'exit' to return to main menu ")
            if user_input_makeup_name.lower() != "exit":
                self.handle_view_makeups_by_name(user_input_makeup_name)
            else:
                self.handle_manage_makeups()
        elif menu_index == 1:
            user_input_makeup_product_type = input("View by product type or 'exit' to return to main menu ")
            if user_input_makeup_product_type.lower() != "exit":
                self.handle_view_makeups_by_product_type(user_input_makeup_product_type)
            else: 
                self.handle_manage_makeups()
        elif menu_index == 2:
            print("View favorites")
            self.handle_view_favorites()
        elif menu_index == 3:
            print("Main Menu")
            self.handle_manage_makeups()
        else:
            self.handle_exit()


# VIEW BY NAME
    def handle_view_makeups_by_name(self, user_input_makeup_name):
        # self.clear_display()
        makeup = Makeup.find_by_makeup_name(user_input_makeup_name)

        if not makeup:
            print("Product name does not exist")
            time.sleep(1)
            self.handle_view_makeups()
        else:
            self.current_makeup = makeup
            makeup_data = [(makeup.id, makeup.name, makeup.brand, makeup.product_type)]
            headers = ["ID", "Name", "Brand", "Type"]
            table = tabulate(makeup_data, headers, tablefmt="fancy_grid")
            print("Makeup available...")
            print(table)
            time.sleep(2)
            self.handle_manage_makeups()


    # VIEW BY PRODUCT TYPE
    def handle_view_makeups_by_product_type(self, user_input_makeup_product_type):
        # self.clear_display()
        makeup_items = Makeup.find_by_product_type(user_input_makeup_product_type)

        if not makeup_items:
            print("Product type does not exist")
            time.sleep(1)
            self.handle_view_makeups()
        else:
            self.current_makeup_product = makeup_items
            makeup_data = [(makeup.id, makeup.name, makeup.brand, makeup.product_type) for makeup in makeup_items]
            headers = ["ID", "Name", "Brand", "Type"]
            table = tabulate(makeup_data, headers, tablefmt="fancy_grid")
            print("Makeup available...")
            print(table)
            time.sleep(2)
            self.handle_manage_makeups()


    #  VIEW FAVORITES
    def handle_view_favorites(self):
        # self.clear_display()
        user_favorites = self.current_user.makeups
        if not user_favorites:
            print("User has no favorites")
            time.sleep(3)
            self.handle_view_makeups()
        else:
            makeup_data = [(makeup.id, makeup.name, makeup.brand, makeup.product_type)for makeup in user_favorites]
            headers = ["ID", "Name", "Brand", "Type"]
            table = tabulate(makeup_data, headers, tablefmt="fancy_grid")
            print("Makeup favorites...")
            print(table)
            time.sleep(2)
            self.handle_manage_makeups()

            
    # CREATE NEW MAKEUP
    def handle_create_new_makeup(self):
        self.clear_display()
        print("Create a new Makeup product\n")
        name = input("Enter Makeup Product Name or type 'exit' to return to main menu: ")
        if name.lower() != "exit":
            if len(name) < 2:
                print("Makeup name must be more than 1 character")
                time.sleep(2)
                self.handle_manage_makeups()
            else:
                existing_makeup = session.query(Makeup).filter_by(name=name).first()
                if existing_makeup:
                    print("Makeup already added")
                    time.sleep(3)
                    self.handle_manage_makeups()
                elif len(name) > 1:
                    brand = input("Enter Makeup Product Brand: ")
                    product_type = input("Enter Makeup Product Category: ")
                    new_makeup_product = Makeup(name=name, brand=brand, product_type=product_type)
                    session.add(new_makeup_product)
                    session.commit()
                    print("Makeup has been added")
                    time.sleep(1)
                    self.handle_manage_makeups()
        else:
            self.handle_manage_makeups()
        

    # DELETE A MAKEUP
    def handle_delete_a_makeup(self):
        self.clear_display()
        print("Delete Makeup")
        makeup_name = input("Enter name of makeup to delete or type 'exit' to return to main menu: ")
        if makeup_name.lower() != "exit":
            makeup = session.query(Makeup).filter_by(name=makeup_name).first()
            if makeup:
                session.delete(makeup)
                session.commit()
                print("Makeup has been deleted")
            else:
                print("Makeup does not exist in database")
            time.sleep(1)
            self.handle_manage_makeups()
        else:
            self.handle_manage_makeups()


# FAVORITE A MAKEUP (ADD TO A LIST)
    def handle_favorite_a_makeup(self, user_id, makeup_name):
        self.clear_display()
        makeup = self.current_makeup
        user = session.query(User).get(user_id)
        makeup = session.query(Makeup).filter_by(name=makeup_name).first()

        if makeup in user.makeups:
            print(f"{user.username} already favorited {makeup.name}")
            time.sleep(3)
            self.handle_manage_makeups()
        elif not makeup:
            print('Makeup does not exist')
            time.sleep(3)
            self.handle_manage_makeups()
        else:
            user.makeups.append(makeup)
            print(f'{makeup.name} added to favorites')
            time.sleep(2)
            self.handle_manage_makeups()
        session.commit()


    # CLEAR DISPLAY
    def clear_display(self):
        os.system("clear")
        print("Welcome to the Makeup Viewer App!")
        print("\n")


    # EXIT
    def handle_exit(self):
        self.clear_display()
        print("Exiting program...")  



app = Cli()
app.start()