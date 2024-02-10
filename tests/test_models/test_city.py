#!/usr/bin/python3
"""unittest City"""
from models.base_model import BaseModel
from models.city import City
import models
import os
import unittest
import pep8


class TestUser(unittest.TestCase):
    """testing City Class"""
    @classmethod
    def setUpClass(cls):
        cls.my_city = City()
        cls.my_city.id = "AA"
        cls.my_city.name = "Addis"

    @classmethod
    def tearDownClass(cls):
        del cls.my_city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            return

    def test_pycodestyle(self):
        """test the pycode style"""
        format = pep8.StyleGuide(quiet=True)
        py = format.check_files(['models/city.py'])
        self.assertEquall(py.total_errors, 0, "fix pep8")

    def test_check_attributes_string(self):
        self.assertEqual(str, type(self.my_city.state_id))
        self.assertEqual(str, type(self.my_city.name))

    def test_check_attributes_present(self):
        attributes = ["name", "state_id", "created_at", "updated_at", "id"]
        for attribute in attributes:
            self.assertIn(attribute, self.my_user.__dict__)

    def test_check_func(self):
        """cheking if City has Docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(self.my_city.__class__, BaseModel))

    def test_save(self):
        self.my_city.save()
        self.assertNotEqual(self.my_city.created_at, self.my_city.updated_at)

    def test_to_dict(self):
        self.assertTrue(hasattr(self.my_city, "to_dict")


if __name__ == "__main__":
    unittest.main()
