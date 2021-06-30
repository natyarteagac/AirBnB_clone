#!/usr/bin/python3
"""
    Creating the Amenity Class Inheritance from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Inheritance from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """Creating new instances from City """
        super().__init__(*args, **kwargs)
        self.name = ""
