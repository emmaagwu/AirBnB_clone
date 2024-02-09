#!/usr/bin/env python3
""" Defines the "Review" class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Represent the Review
    Attributes:
        place_id(str) - The place id(Place.id)
        user_id(str) - The user id (User.id)
        text(str) - The review text
    """

    place_id = ""
    user_id = ""
    text = ""
