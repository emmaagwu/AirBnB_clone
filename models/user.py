#!/usr/bin/env python3
""" Defines the "USER" class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Represents a User
    Attributes:
        email(str) - email of the user
        password(str) - password of the user
        first_name(str) - first name of the user
        last_name(str) - Last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
