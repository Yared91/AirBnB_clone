#!/usr/bin/python3
"""unittest Place"""
from models.base_model import BaseModel
from models.place import Place
import models
import os
import unittest
import pep8


class TestPlace(unittest.TestCase):
    """testing Place Class"""

    def test_pycodestyle(self):
        """test the pycode style"""
        style = pep8.StyleGuide(quiet=True)
        py = style.check_files(['models/place.py'])
        self.assertEquall(py.total_errors, 0, "fix pep8")

    def test_check_attributes_string(self):
        self.assertEqual(str, type(Place.city_id))
        self.assertEqual(str, type(Place.user_id))
        self.assertEqual(str, type(Place.name))
        self.assertEqual(str, type(Place.description))
        self.assertEqual(int, type(Place.number_rooms))
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertEqual(int, type(Place.max_guest))
        self.assertEqual(int, type(Place.price_by_night))
        self.assertEqual(float, type(Place.latitude))
        self.assertEqual(float, type(Place.longitude))
        self.assertEqual(list, type(Place.amenity_ids))

    def test_check_attributes_present(self):
        attributes = ["city_id", "user_id", "name", "id", "created_at",
                      "updated_at", "description", "number_rooms", "number_bathrooms",
                      "max_guest", "price_by_night", "latitude", "longitude", "amenity_ids"]
        for attribute in attributes:
            self.assertIn(attribute, Place.__dict__)

    def test_check_func(self):
        """checking if Place has Docstring"""
        self.assertIsNotNone(Place.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(Place.__class__, BaseModel))

    def test_save(self):
        Place.save()
        self.assertNotEqual(Place.created_at, Place.updated_at)

    def test_to_dict(self):
        self.assertTrue(hasattr(Place, "to_dict"))


if __name__ == "__main__":
    unittest.main()
