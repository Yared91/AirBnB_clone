#!/usr/bin/python3
"""unittest Review"""
from models.base_model import BaseModel
from models.review import Review
import models
import os
import unittest
import pep8


class TestReview(unittest.TestCase):
    """testing Review Class"""

    def test_pycodestyle(self):
        """test the pycode style"""
        style = pep8.StyleGuide(quiet=True)
        py = style.check_files(['models/review.py'])
        self.assertEquall(py.total_errors, 0, "fix pep8")

    def test_check_attributes_string(self):
        self.assertEqual(str, type(Review.place_id))
        self.assertEqual(str, type(Review.user_id))
        self.assertEqual(str, type(Review.text))

    def test_check_attributes_present(self):
        attributes = ["place_id", "id", "created_at", "updated_at",
                      "user_id", "text"]
        for attribute in attributes:
            self.assertIn(attribute, Review.__dict__)

    def test_check_func(self):
        """checking if Review has Docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_check_subclass(self):
        """checking for subclass in the Supper class"""
        self.assertTrue(issubclass(Review.__class__, BaseModel))

    def test_save(self):
        Review.save()
        self.assertNotEqual(Review.created_at,
                            Review.updated_at)

    def test_to_dict(self):
        self.assertTrue(hasattr(Review, "to_dict"))


if __name__ == "__main__":
    unittest.main()
