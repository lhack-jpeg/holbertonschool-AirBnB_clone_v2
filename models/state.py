#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City



class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(), nullable=False)
    cities = relationship("City", backref="state")

    # I think more needs to be added. Need to add a getter
    # for the FileStorage and I think we may have to have an if/else
    # statement to check if it's in db storage or filestorage
