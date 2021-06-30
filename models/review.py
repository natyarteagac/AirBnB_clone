#!/usr/bin/python3
"""
    Creating the Review Class Inheritance from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        Inheritance from BaseModel
    """
    self.place_id = ""
    self.user_id = ""
    self.text = ""
