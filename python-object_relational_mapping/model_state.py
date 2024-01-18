from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# creating a declarative base that we will inherit from
Base = declarative_base()

class State(Base):
    # creating a class
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
