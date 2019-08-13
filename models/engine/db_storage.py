#!/usr/bin/python3
""" Database Storage Engine """
from sqlalchemy import (create_engine)


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
        if cls=None:
            result = self.__session.query().all():

