#!/usr/env/ pythom3
""" Defines the "Amenity" class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an Amenity
    Attribute:
        name(str) - name of an Amenity
     """

    name = ""
