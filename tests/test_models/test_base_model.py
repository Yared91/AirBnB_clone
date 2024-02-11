#!/usr/bin/python3
"""unittest BaseModel"""
from models.base_model import BaseModel
import unittest
import models
import os
import pep8


class TestBaseModel(unittest.TestCase):
    """Testing attributes of BaseModel"""

    def test_pycodstyle(self):
        """test the pycode style"""
        style = pep8.StyleGuide(quiet=True)
        py = style.check_files(['models/base_model.py'])
        self.assertEquall(py.total_errors, 0, "fix pep8")

    def test_save(self):
        """checking created_at and updated_at date aren't equal"""
        BaseModel.save()
        self.assertNotEqual(BaseModel.created_at,
        BaseModel.updated_at)

    def test_to_dict(self):
        my_model_dict = BaseModel.to_dict()
        self.assertEqual(BaseModel.__clas__.__name__, "BaseModel")
        self.assertTrue(isinstance(my_model_dict["created_at"], str))
        self.assertTrue(isinstance(my_model_dict["updated_at"], str))

    def test_check_fun(self):
        """checking if functions have docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_check_attributes(self):
        """checks if BaseModel has Attributes and are callable"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(callable(BaseModel.__init__))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(callable(BaseModel.save))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(callable(BaseModel.to_dict))


if __name__ == "__main__":
    unittest.main()
