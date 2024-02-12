#!/usr/bin/python3
"""unittest BaseModel"""
from models.base_model import BaseModel
import unittest
import models
import os
import pep8
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Testing attributes of BaseModel"""

    def test_pycodstyle(self):
        """test the pycode style"""
        style = pep8.StyleGuide(quiet=True)
        py = style.check_files(['models/base_model.py'])
        self.assertEqual(py.total_errors, 2, "fix pep8")

    def test_save(self):
        """checking created_at and updated_at date aren't equal"""
        md = BaseModel()
        md.save()
        self.assertNotEqual(md.created_at, md.updated_at)

    def test_check_fun(self):
        """checking if functions have docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_check_attributes(self):
        """checks if BaseModel has Attributes"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_run(self):
        """checks if the BaseModel is initialized"""
        self.assertIsNotNone(BaseModel().id)
        self.assertIsNotNone(BaseModel().created_at)
        self.assertIsInstance(BaseModel().created_at, datetime)
        self.assertIsNotNone(BaseModel().updated_at)
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_to_dict(self):
        """cheking to_dict Method"""
        new_dict = dict(BaseModel().__dict__)
        new_dict["created_at"] = BaseModel().created_at.isoformat()
        new_dict["updated_at"] = BaseModel().updated_at.isoformat()
        new_dict["__class__"] = type(BaseModel()).__name__
        self_assertEqual(new_dict, BaseModel().to_dict())

    def test_check_keys(self):
        """ testing **kwargs with valid and in valid __init__"""
        valid_kwarg = {
                "my_number": "89",
                "name": "My First Model",
                "__class__": "BaseModel",
                "updated_at": "2017-09-28T21:05:54.119572",
                "id": "b6a6e15c-c67d-4312-9a75-9d084935e579",
                "created_at": "2017-09-28T21:05:54.119427",
                }
        kw1 = BaseModel(**valid_kwarg)

        updated_at = datetime.fromisoformat(valid_kwarg["updated_at"])
        valid_kwarg["updated_at"] = updated_at
        created_at = datetime.fromisoformat(valid_kwarg["created_at"])
        valid_kwarg["created_at"] = created_at

        for k, v in valid_kwarg.items():
            if k not in ["__class__"]:
                self.assertEqual(getattr(kw1, k, None), v)
        invalid_kwarg = {
                "my_number": "89",
                "name": "My First Model",
                "__class__": "BaseModel",
                "updated_at": "2017-09-28T21:05:54.119572",
                "id": "b6a6e15c-c67d-4312-9a75-9d084935e579",
                "created_at": "2017-09-28T21:05:54.119427",
        }
        with self.assertRaises(TypeError):
            kw2 = BaseModel(**invalid_kwarg)
        try:
            obj = self.__objects['BaseModel.c3835cc2-d764-4a2b-a0ce-406f4d13bef2']
        except KeyError:
            print("Object not found in dictionary")
    def test_str_(self):
        """ checking the style  __str__"""
        str1 = " [{}] ({}) {}".format(type(BaseModel()).__name__, BaseModel().id, BaseModel().__dict__)
        self.assertEqual(str1, str(BaseModel()))


if __name__ == "__main__":
    unittest.main()
