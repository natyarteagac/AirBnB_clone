#!/usr/bin/python3
"""
    Defines all common attributes/methods for other classes from BaseModel
"""

from uuid import uuid4
from datetime import datetime


class BaseModel():

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        aux = {
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
        }
        dict_copy = self.__dict__.copy()
        dict_copy.update(aux)
        return dict_copy
