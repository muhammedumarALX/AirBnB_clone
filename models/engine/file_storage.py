#!/usr/bin/python3
import json
import models


class FileStorage:
    """class that seriailizes/deserializes instance to JSON"""
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Instance method to return dictionary"""
        return self.__objects

    def new(self, obj):
        """Instance method setting in an object with key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Instance method to serialize object to JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {k : v.to_dict() for k,v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Instance method to deserialize JSON file to object"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for ob in obj_dict.values():
                    cls_name = ob['__class__']
                    del ob['__class__']
                    self.new(eval(cls_name)(**ob))

        except FileNotFoundError:
            return
