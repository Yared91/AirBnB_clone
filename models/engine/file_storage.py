#!/usr/bin/python3
"""FileStorage Class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """"sets in __objects the obj with key <obj class name>.id"""
        obj = self.__objects["{}.{}"
                .format(obj.__class__.__name__, obj.id)]

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic_json = {obj: self.__objects[obj].to_dict()
                for obj in self.__objects.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(dic_json, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        subclass_dict = {'BaseModel': BaseModel, 'Userr': User, 'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}

        try:
            fstorage = self.__file_path
            with open(fstorage, "r") as f:
                dic_json = json.load(f)
                for k, v in dic_json.items():
                    subclass = v['__class__']
                    subclass_inst = subclass_dict.get(subclass)
                    if subclass_inst:
                        inst = subclass_inst(**v)
                        obj = self.all()
                        obj[k] = inst
        except FileNotFoundError:
            pass
