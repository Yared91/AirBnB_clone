#!/usr/bin/python3
"""unittest Review"""
from models.base_model import BaseModel
from models.review import Review
import models
import os
import unittest


class TestUser(unittest.TestCase):
    """testing Review Class"""
    @classmethod
    def setUpClass(cls):
        cls.my_review = Review()
        cls.my_review.place_id = "Addis"
        cls.my_review.user_id = "Elilta"
        cls.my_review.text = "First"

    @classmethod
    def tearDownClass(cls):
        del cls.my_review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            return

    def test_check_attributes_string(self):
        self.assertEqual(str, type(self.my_review.place_id))
        self.assertEqual(str, type(self.my_review.user_id))
        self.assertEqual(str, type(self.my_review.text))

    def test_check_attributes_present(self):
        attributes = ["place_id", "id", "created_at", "updated_at",
                "user_id", "text"]
        for attribute in attributes:
            self.assertIn(attribute, self.my_review.__dict__)

    def test_check_func(self):
        """cheking if Review has Docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(self.my_review.__class__, BaseModel))

    def test_save(self):
        self.my_review.save()
        self.assertNotEqual(self.my_review.created_at,
                self.my_review.updated_at)

    def test_to_dict(self):
        self.assertTrue(hasattr(self.my_review, "to_dict")

if __name__ == "__main__":
    unittest.main()
