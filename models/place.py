#!/usr/bin/env python3
""" Defines the "Place" class """
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a PLace
    Attributes:
        city_id(str) - city_id of the place
        user_id(str) - user_id of the place
        name(str) - name of the place
        description(str) - description of the place
        number_rooms(int) - number_rooms of the place
        number_bathrooms(int) - number_bathrooms of then place
        max_guest(int) - max_guest of the place
        price_by_night(int) - price_by_night of the place
        latitude(float) - latitude of the place
        longitude(float) - longitude of the place
        amenity_ids(str) - amenity_ids of the place
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
