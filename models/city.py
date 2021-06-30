#!/usr/bin/python3
"""
    Creating the City Class Inheritance from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
        Inheritance from BaseModel
    """

    state_id = ""
    name = ""
