#!/usr/bin/python3
'''Module contains the engine for the db storage.'''

from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    '''Attributes will get system info to start engine.'''
    __engine = None
    __session = None

    def __init__(self):
        '''Creates the engine for SQLALCHEMY.'''
        dialect = 'mysql'
        driver = 'mysqldb'
        sql_user = getenv('HBNB_MYSQL_USER')
        sql_pass = getenv('HBNB_MYSQL_PWD')
        sql_host = getenv('HBNB_MYSQL_HOST')
        sql_db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f"{dialect}+{driver}://{sql_user}:{sql_pass}@{sql_host}/{sql_db}",
            pool_pre_ping=True
        )

        if sql_user == 'test':  # Drop all tables is test_user for QOL.
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        Queries the Database, depending on the object passed through.
        if cls=None, queries all types of objects and returns as dict similar to
        Filestorage.
        key = <class-name>.<object-id>
        value = obj.
        '''
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        obj_dict = {}
        if cls is not None:
            query = self.__session.query(cls).all()
            for row in query:
                id = row.id
                key = f'{cls}.{id}'
                print('key: ', key)
                print('row__DICT: ', row.__dict__)

    def new(self, obj):
        '''Add the object to the current sesison.'''
        self.reload()
        with self.__session.begin():
            self.__session.add(obj)
            self.save()  # Will automatically close session when finished

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.reload()
            self.__session().delete(obj)
            self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(expire_on_commit=False)
        self.__session = scoped_session(Session)
