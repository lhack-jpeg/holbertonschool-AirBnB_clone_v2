#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.base_model import BaseModel, Base

from os import getenv

storage_method = getenv('HBNB_TYPE_STORAGE')

if storage_method == 'db':
    storage = DBStorage()
    storage.reload()
else:
    print('Filestorage')
    storage = FileStorage()
    storage.reload()
