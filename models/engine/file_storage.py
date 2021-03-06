#!/usr/bin/python3
"""
Writing a class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances

"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a
    JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with the key
        """
        object_id = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[object_id] = obj

    def save(self):
        """
        Serializes __object to the JSON file
        """
        aux_list = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            for key in FileStorage.__objects:
                aux_list[key] = self.__objects[key].to_dict()
            f.write(json.dumps(aux_list))

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_file = json.loads(f.read())
                for key, value in json_file.items():
                    class_name = key.split(".")[0]
                    FileStorage.__objects[key] = eval(class_name)(**value)
        except Exception as ex:
            pass
