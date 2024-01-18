from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

# creating the engine and session
engine = create_engine('mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)
session = Session()

# returning all states with the letter a from the table and printing them
states = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()
for i in states:
    print("{}: {}".format(i.id, i.name))

# closing the session
session.close()
