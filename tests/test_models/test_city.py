#!/usr/bin/python3
"""unittest City"""
from models.base_model import BaseModel
from models.city import City
import models
import os
import unittest
import pep8


class TestCity(unittest.TestCase):
    """testing City Class"""

    def test_city_subclass(self):
        """tests city subclass"""

        """checks if the object of city are strings"""
        self.assertEqual(str, type(City.state_id))
        self.assertEqual(str, type(City.name))

        """checks if the instances are in dictionary style"""
        attributes = ["name", "state_id", "created_at", "updated_at", "id"]
        for attribute in attributes:
            self.assertIn(attribute, City.__dict__)

        """checking if City has Docstring"""
        self.assertIsNotNone(City.__doc__)

        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(City.__class__, BaseModel))

        """checks if the created_at and updated_at are saved"""
        self.my_city.save()
        self.assertNotEqual(City.created_at, City.updated_at)

        """checks if the dictionary has city attributes"""
        self.assertTrue(hasattr(City, "to_dict"))


if __name__ == "__main__":
    unittest.main()
