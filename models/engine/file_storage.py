#!/usr/bin/python3
"""FileStorage Class"""
import json


class FileStorage:
    """
    FileStorage Class

    Attributes:
    __file_path(str): file.json
    __objects: dictionary
    all(self): return dictionary
    new(self, obj): new object entered
    save(self): saves object
    reload(self): it reloads for new entry
    """

    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def get_classes(attr):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        attributes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        return attributes.get(attr)

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """"sets in __objects the obj with key <obj class name>.id"""
        obj = self.__objects["{}.{}"
                             .format(obj.__class__.__name__, obj.id)]

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new = self.__objects
        dic_json = {obj: new[obj].to_dict() for obj in new.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(dic_json, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            self.__objects.clear()
            obj_load = {}
            try:
                fstorage = self.__file_path
                with open(fstorage, "r") as f:
                    obj_load = json.load(f)
            except Exception:
                pass
            for k, v in obj_load.items():
                attr = v.get("__class__")
                subclass = self.get_classes(attr)

                if subclass is None:
                    raise Exception("Error: Invalid class name"
                                    .format(attr))
                    self.__objects[k] = subclass(**v)
        except FileNotFoundError:
            pass
