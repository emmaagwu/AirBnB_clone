#!/usr/bin/env python3
""" Defines the "state" class """
from models.base_model import BaseModel


class State(BaseModel):
    """ Represents a State
    Attributes:
        name(str) - name of the state
    """

    name = ""
