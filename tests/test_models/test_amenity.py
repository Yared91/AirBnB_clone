#!/usr/bin/python3
"""unittest Amenity"""
from models.base_model import BaseModel
from models.amenity import Amenity
import models
import os
import unittest
import pep8


class TestUser(unittest.TestCase):
    """ testing Amenity Class"""
    @classmethod
    def setUpClass(cls):
        cls.my_amenity = Amenity()
        cls.my_amenity.name = "Serenity"

    @classmethod
    def tearDownClass(cls):
        del cls.my_amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            return

    def test_pycodestyle(self):
        """test the pycode style"""
        format = pep8.StyleGuide(quiet=True)
        py = format.check_files(['models/amenity.py'])
        self.assertEquall(py.total_errors, 0, "fix pep8")


    def test_check_attributes_string(self):
        self.assertEqual(str, type(self.my_amenity.name))

    def test_check_attributes_present(self):
        attributes = ["name", "id", "created_at", "updated_at"]
        for attribute in attributes:
            self.assertIn(attribute, self.my_amenity.__dict__)

    def test_check_func(self):
        """cheking if Amenity has Docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(self.my_amenity.__class__, BaseModel))

    def test_save(self):
        self.my_amenity.save()
        self.assertNotEqual(self.my_amenity.created_at, self.my_amenity.updated_at)

    def test_to_dict(self):
        self.assertTrue(hasattr(self.my_amenity, "to_dict")


if __name__ == "__main__":
    unittest.main()
