#!/usr/bin/python3
"""FileStorage Class"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
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

    __file_path = file.json
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """"sets in __objects the obj with key <obj class name>.id"""
        obj = Filestorage.__objects["{}.{}"
                .format(obj.__class__.__name__, obj.id)]

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic_json = {obj: FileStorage.__objects[obj].to_dict()
                for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dic_json, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            fstorage = FileStorage.__file_path
            with open(fstorage) as f:
                dic_json = json.load(f)
                for k in dic_json.values():
                    del k["__class__"]
                    self.new(eval(k["__class__"])(**k))
        except FileNotFoundError:
            pass
