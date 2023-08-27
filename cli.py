from simple_term_menu import TerminalMenu
from sqlalchemy import create_engine
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




app = Cli()
app.start()