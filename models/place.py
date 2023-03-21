#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
import models
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Table
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey(
        'cities.id', ondelete="CASCADE"), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True, default=None)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True, default=None)
    longitude = Column(Float, nullable=True, default=None)
    amenity_ids = []
    user = relationship("User", back_populates='places')
    cities = relationship("City", back_populates='places')
    reviews = relationship(
        "Review", back_populates='places', cascade='all, delete-orphan')

    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(String(60), "place_id", ForeignKey("places.id", ondelete="CASCADE"),
               primary_key=True, nullable=False),
        Column(String(60), "amenity_id", ForeignKey("amenities.id", ondelete="CASCADE"),
               primary_key=True, nullable=False)
    )

    amenities = relationship(
        "Amenity", back_populates='places', secondary=place_amenity, viewonly=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            new_ls = []
            for rev in models.storage.all(Review):
                if self.id == Review.place_id:
                    new_ls.append(rev)
            return new_ls
