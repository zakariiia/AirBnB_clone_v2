#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.place import Place
from models.review import Review
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user."""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user",
                        cascade='all, delete, delete-orphan')