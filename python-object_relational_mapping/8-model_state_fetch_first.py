from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

# creating the engine and session
engine = create_engine('mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)
session = Session()

# returning the first state in the table and printing it 
state = session.query(State).order_by(State.id).first()
if state:
    print("{}: {}".format(state.id ,state.name))
else:
    print("Nothing")

# closing the session
session.close()