#!/usr/bin/python3
"""unittest Place"""
from models.base_model import BaseModel
from models.place import Place
import models
import os
import unittest


class TestUser(unittest.TestCase):
    """testing Place Class"""
    @classmethod
    def setUpClass(cls):
        cls.my_place = Place()
        cls.my_place.city_id = "Bahamas"
        cls.my_place.user_id = "Maldevis"
        cls.my_place.name = "The Beach"
        cls.my_place.description = "Heaven on Earth"
        cls.my_place.number_rooms = 0
        cls.my_place.number_bathrooms = 0
        cls.my_place.max_guest = 0
        cls.my_place.price_by_night = 0
        cls.my_place.latitude = 0.0
        cls.my_place.longitude = 0.0
        cls.my_place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        del cls.my_place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            return

    def test_check_attributes_string(self):
        self.assertEqual(str, type(self.my_place.city_id))
        self.assertEqual(str, type(self.my_place.user_id))
        self.assertEqual(str, type(self.my_place.name))
        self.assertEqual(str, type(self.my_place.description))
        self.assertEqual(int, type(self.my_place.number_rooms))
        self.assertEqual(int, type(self.my_place.number_bathrooms))
        self.assertEqual(int, type(self.my_place.max_guest))
        self.assertEqual(int, type(self.my_place.price_by_night))
        self.assertEqual(float, type(self.my_place.latitude))
        self.assertEqual(float, type(self.my_place.longitude))
        self.assertEqual(list, type(self.my_place.amenity_ids))

    def test_check_attributes_present(self):
        attributes = ["city_id", "user_id", "name", "id", "created_at",
                "updated_at", "description", "number_rooms", "number_bathrooms"
                ,"max_guest", "price_by_night", "latitude", "longitude", "amenity_ids"]
        for attribute in attributes:
            self.assertIn(attribute, self.my_place.__dict__)

    def test_check_func(self):
        """cheking if Place has Docstring"""
        self.assertIsNotNone(Place.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(self.my_place.__class__, BaseModel))

    def test_save(self):
        self.my_place.save()
        self.assertNotEqual(self.my_place.created_at, self.my_place.updated_at)

    def test_to_dict(self):
        self.assertTrue(hasattr(self.my_place, "to_dict")

if __name__ == "__main__":
    unittest.main()
