#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models.engine.file_storage
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete")

    # I think more needs to be added. Need to add a getter
    # for the FileStorage and I think we may have to have an if/else
    # statement to check if it's in db storage or filestorage
    else:
        @property
        def cities(self):
            '''
            If in filestorage mode this will
            return a list with all cities that have the state_id as
            a foreign key reference.
            '''
            city_list = []
            '''
            Use the method from filestorage to return list of cities.
            Currently no way toi truncate list, will just be dict that is
            filtered through.
            '''
            city_dict = models.storage.all(City).values()
            for city in city_dict:
                if city['state_id'] == self.id:
                    city_list.append(city)
            return city_list
