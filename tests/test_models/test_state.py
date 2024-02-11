#!/usr/bin/python3
"""unittest State"""
from models.base_model import BaseModel
from models.state import State
import models
import os
import unittest
import pep8


class TestState(unittest.TestCase):
    """testing State Class"""

    def test_pycodestyle(self):
        """test the pycode style"""
        style = pep8.StyleGuide(quiet=True)
        py = style.check_files(['models/state.py'])
        self.assertEqual(py.total_errors, 0, "fix pep8")

    def test_check_attributes_string(self):
        self.assertEqual(str, type(State.name))

    def test_check_attributes_present(self):
        attributes = ["name"]
        for attribute in attributes:
            self.assertIn(attribute, State.__dict__)

    def test_check_func(self):
        """checking if State has Docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_save(self):
        State.save(self)

    def test_to_dict(self):
        self.assertTrue(hasattr(State, "to_dict"))


if __name__ == "__main__":
    unittest.main()
