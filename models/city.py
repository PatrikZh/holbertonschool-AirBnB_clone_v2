#!/usr/bin/python3
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from models.base_model import BaseModel, Base
0
""" City Module for HBNB project """


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey(
        'states.id', ondelete="CASCADE"), nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship("State", back_populates="cities")
    places = relationship('Place', back_populates='cities',
                          cascade='all, delete-orphan')
