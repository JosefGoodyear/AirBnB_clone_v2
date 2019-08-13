#!/usr/bin/python3
""" Database Storage Engine """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base


class DBStorage:
    """
    This class is the database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize an instance
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """
        query all objects from the current db session, based on class name
        """
        if cls = None:
            result = self.__session.query(User, State, City, Amenity, Place, Review).all()
        else:
            result = self.__session.query(cls).all()
        result_dict = {}
        for row in results:
            key = ".".join([type(row).__name__,row.id])
            result_dict[key] = row
        return result_dict

    def new(self, obj):
        """
        add the object to the current databse session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        commit changes to the current database session
        """
        self.__session.commit()
    def delete(self, obj=None):
        """
        delete obj from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self)
        """
        create all tables in the database
        """
        Base.metadata.create_all(engine)
        self.__session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
