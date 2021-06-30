#!/usr/bin/python3
"""
    Creating the User Class Inheritance from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        Inheritance from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
