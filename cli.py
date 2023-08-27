from simple_term_menu import TerminalMenu
from sqlalchemy import create_engine
import time
from models import User, Makeup
from sqlalchemy.orm import sessionmaker

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
            self.handle_favorite_a_makeup()
        else:
            self.handle_exit()




app = Cli()
app.start()