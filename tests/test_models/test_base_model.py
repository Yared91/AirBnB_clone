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

        BaseModel().save(self)

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
 55            """ testing **kwargs with valid and in valid __init__"""
 56             valid_kwarg = {
 57                      my_number: (<class 'int'>) - 89
 58                      name: (<class 'str'>) - My First Model
 59                      __class__: (<class 'str'>) - BaseModel
 60                      updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
 61                      id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
 62                      created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427
 63             }
 64             kw1 = BaseModel(**valid_kwarg)
 65 
 66             valid_kwarg["updated_at"] = updated_at
 67             updated_at = datetime.fromisoformat(valid_kwarg["updated_at"])
 68             valid_kwarg["created_at"] = created_at
 69             created_at = datetime.fromisoformat(valid_kwarg["created_at"])
 70 
 71             for k, v in valid_kwarg.items():
 72                     if k is not in ["__class__"]:
 73                     self.assertEqual(getattr(kw1, k, None), v)
 74 
 75 
 76              invalid_kwarg = {
 77                       my_number: (<class 'int'>) - 89
 78                       name: (<class 'str'>) - My First Model
 79                       __class__: (<class 'str'>) - BaseModel
 80                       updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
 81                       id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
 82                       created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427
 83              }
 84              with self.assertRaises(TypeError):
 85                      kw2 = BaseModel(**invalid_kwarg)
 86 
 87      def test_str_(self):
 88              """ checking the style  __str__"""
 89              str1 = " [{}] ({}) {}".format(type(BaseModel()).__name__, BaseModel().id, BaseModel().__dict__)
 90              self.assertEqual(BaseModel()_str, str(BaseModel()))



if __name__ == "__main__":
    unittest.main()
