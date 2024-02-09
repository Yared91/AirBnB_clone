#!/usr/bin/python3
"""unittest State"""
from models.base_model import BaseModel
from models.state import State
import models
import os
import unittest


class TestUser(unittest.TestCase):
    """testing State Class"""
    @classmethod
    def setUpClass(cls):
        cls.my_state = State()
        cls.my_state.name = "Addis Ababa"

    @classmethod
    def tearDownClass(cls):
        del cls.my_state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            return

    def test_check_attributes_string(self):
        elf.assertEqual(str, type(self.my_state.name))

    def test_check_attributes_present(self):
        attributes = ["name", "id", "created_at", "updated_at"]
        for attribute in attributes:
            self.assertIn(attribute, self.my_user.__dict__)

    def test_check_func(self):
        """cheking if State has Docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(self.my_state.__class__, BaseModel))

    def test_save(self):
        self.my_state.save()
        self.assertNotEqual(self.my_state.created_at, self.my_state.updated_at)

    def test_to_dict(self):
        self.assertTrue(hasattr(self.my_state, "to_dict")

if __name__ == "__main__":
    unittest.main()
