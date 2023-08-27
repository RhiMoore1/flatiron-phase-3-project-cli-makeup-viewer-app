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
 




app = Cli()
app.start()