#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
import models.amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models.engine.file_storage


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60),
           ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False),
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

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

    @property
    def reviews(self):
        '''
        In filestorage mode, this will return a list of dictionaries.
        Where the place_id in review will be equal to place.id in the
        place obj.
        '''
        review_list = []
        fs = file_storage.File_storage()

        review_dict = fs.all(Review.__class__.__name__)
        for review in review_dict:
            if review.get('place.id') == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenity(self):
        '''
        In filestorage mode will return a list of dictionaries where
        instances contain contain amenity id linked to the place object.
        place.amenity_id == amenity.id
        '''
        amenity_list = []
        fs = file_storage.File_storage()

        amenity_dict = fs.all(amenity.Amenity.__class__.__name__)
        for amenity in amenity_dict:
            if amenity.get('amenity.id') == self.amenity_id:
                amenity_list.append(amenity)
        return amenity_list

    @amenity.setter
    def amenity(self, amenity):
        if amenity.__class__.__name__ == 'Amenity':
            self.amenity_id.append(amenity.id)
        else:
            pass
