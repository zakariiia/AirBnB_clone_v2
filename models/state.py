#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from models.base_model import Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """State class is the subclass of BaseModel and Base"""
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", 
                        cascade="delete,all, delete, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """getter attribute cities that returns the list of City."""
            c_list = []
            for c in list(models.storage.all(City).values()):
                if c.state_id == self.id:
                    c_list.append(c)
            return c_list

