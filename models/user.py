#!/usr/bin/python3
"""
    Creating the User Class Inheritance from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        Inheritance from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """Creating new instances from User """
        super().__init__(*args, kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
