#!/usr/bin/python3
"""unittest BaseModel"""
from models.base_model import BaseModel
import unittest
import models
import os


class TestBaseModel(unittest.TestCase):
    """Testing attributes of BaseModel"""
    @classmethod
    def setUpClass(cls):
        cls.my_model = BaseModel()
        cls.my_model.name = "My First Model"
        cls.my_model.my_number = 89

    @classmethod
    def tearDownClass(cls):
        del cls.my_model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            return

    def test_save(self):
        """checking created_at and updated_at date aren't equal"""
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at,
        self.my_model.updated_at)

    def test_instance_of_class(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_to_dict(self):
        my_model_dict = self.my_model.to_dict()
        self.assertEqual(self.my_model.__clas__.__name__, "BaseModel")
        self.assertTrue(isinstance(my_model_dict["created_at"], str))
        self.assertTrue(isinstance(my_model_dict["updated_at"], str))

    def test_check_fun(self):
        """cheking if functions have docstring"""
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
