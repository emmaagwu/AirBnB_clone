#!/usr/bin/env python3
""" Defines the "City" class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a City
    Attributes:
        state_id(str) - The state id(State.id)
        name(str) - The name of the city.
    """

    state_id = ""
    name = ""
