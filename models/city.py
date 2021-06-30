#!/usr/bin/python3
"""
    Creating the City Class Inheritance from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
        Inheritance from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """Creating new instances from City """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
