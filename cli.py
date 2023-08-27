from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///makeup_data.db')
Session = sessionmaker(bind=engine)
session = Session()



class Cli():
    pass

app = Cli()
app.start()