#!/usr/bin/python3
"""unittest User"""
from models.base_model import BaseModel
from models.user import User
import models
import os
import unittest


class TestUser(unittest.TestCase):
    """ testing User Class"""

    def pycodestyle(self):
        """test the pycode style"""
        style = pep8.StyleGuide(quiet=True)
        py = style.check_files(['models/user.py'])
        self.assertEqual(py.total_errors, 0, "fix pep8")

    def test_check_attributes_string(self):
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))

    def test_check_attributes_present(self):
        attributes = ["email", "password", "first_name", "last_name"]
        for attribute in attributes:
            self.assertIn(attribute, User.__dict__)

    def test_check_func(self):
        """checking if User has Docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_save(self):
        User.save(self)

    def test_to_dict(self):
        self.assertTrue(hasattr(User, "to_dict"))


if __name__ == "__main__":
    unittest.main()
