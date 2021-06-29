#!/usr/bin/python3
"""
    Defines all common attributes/methods for other classes from BaseModel


"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """BaseModel class with *args and **kwargs atributes"""

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Return class name, self id and self dictionary"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update datetime of atribute self.updated_at"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Return all the atributes of the class"""
        aux = {
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
        }
        dict_copy = self.__dict__.copy()
        dict_copy.update(aux)
        return dict_copy
