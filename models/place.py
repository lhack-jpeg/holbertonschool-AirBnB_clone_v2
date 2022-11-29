#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models.engine.file_storage
from os import getenv


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60),
           ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete'
        )
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            back_populates='place_amenities',
            viewonly=False
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            '''
            In filestorage mode, this will return a list of dictionaries.
            Where the place_id in review will be equal to place.id in the
            place obj.
            '''
            from models.review import Review
            review_list = []

            review_dict = models.storage.all(Review)
            for review in review_dict:
                if review['place.id'] == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            '''
            In filestorage mode will return a list of dictionaries where
            instances contain contain amenity id linked to the place object.
            place.amenity_id == amenity.id
            '''
            from models.amenity import Amenity
            amenity_list = []

            amenity_dict = models.storage.all(Amenity)
            for amenity in amenity_dict:
                if amenity['amenity.id'] == self.amenity_id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity):
            if amenity.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(amenity.id)
            else:
                pass
