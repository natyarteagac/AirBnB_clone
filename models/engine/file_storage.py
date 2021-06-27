#!/usr/bin/python3
"""
Writing a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
"""
import json


class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with the key"""
        object_id = obj.__class__.__name__ + '.' + obj.id
        self.__objects[object_id] = obj

    def save(self):
        """Serializes __object to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            if self.__file_path:
                with open(self.__file_path, "r", encoding="utf-8") as f:
                    return (json.load(f))
        except Exception as ex:
            pass
