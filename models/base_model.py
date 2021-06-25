#!/usr/bin/python3
"""
    Defines all common attributes/methods for other classes from BaseModel
"""

import cmd
from uuid import uuid4
from datetime import datetime


class BaseModel(cmd.Cmd):

    def __init__(self):
        self.id = uuid4()
        self.created_at = datetime.now()
        #self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({})".format(self.__class__.__name__, self.id)

    # def do_EOF(self, line):
        # return True

# if __name__ == '__main__':
    # HelloWorld().cmdloop()


my_object = BaseModel()
print(my_object.__str__())
