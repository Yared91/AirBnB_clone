#!/usr/bin/python3
"""unittest Amenity"""
from models.base_model import BaseModel
from models.amenity import Amenity
import models
import os
import unittest
import pep8


class TestAmenity(unittest.TestCase):
    """ testing Amenity Class"""

    def test_pycodestyle(self):
        """test the pycode style"""
        style = pep8.StyleGuide(quiet=True)
        py = style.check_files(['models/amenity.py'])
        self.assertEquall(py.total_errors, 0, "fix pep8")

    def test_check_attributes_string(self):
        self.assertEqual(str, type(Amenity.name))

    def test_check_attributes_present(self):
        attributes = ["name", "id", "created_at", "updated_at"]
        for attribute in attributes:
            self.assertIn(attribute, Amenity.__dict__)

    def test_check_func(self):
        """cheking if Amenity has Docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(Amenity.__class__, BaseModel))

    def test_save(self):
        Amenity.save()
        self.assertNotEqual(Amenity.created_at, Amenity.updated_at)

    def test_to_dict(self):
        self.assertTrue(hasattr(Amenity, "to_dict"))


if __name__ == "__main__":
    unittest.main()
