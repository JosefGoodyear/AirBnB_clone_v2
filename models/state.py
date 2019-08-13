#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade="all, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        city_list = []
        for city in self.cities:
            if self.id == city.state_id:
                city_list.append(city)
        return city_list
