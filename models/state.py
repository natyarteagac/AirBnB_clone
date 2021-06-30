#!/usr/bin/python3
"""
    Creating State class Inheritance from BaseModel


"""
from models.base_model import BaseModel


class State(BaseModel):
    def __init__(self, *args, **kwargs):
        """Creating new instances from State """
        super().__init__(*args, **kwargs)
        self.name = ""
