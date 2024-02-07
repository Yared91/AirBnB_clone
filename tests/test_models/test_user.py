#!/usr/bin/python3
"""unittest User"""
from models.base_model import BaseModel
from models.user import User
import models
import os
import unittest


class TestUser(unittest.TestCase):
	""" testing User Class"""
	@classmethod
	def setUpClass(cls):
		cls.my_user = User()
		cls.my_user.first_name = "Betty"
		cls.my_user.last_name = "Bar"
		cls.my_user.email = "airbnb@mail.com"
		cls.my_user.password = "root"

	@classmethod
	def tearDownClass(cls):
		del cls.my_user
		try:
		    os.remove("file.json")
		except FileNotFoundError:
		    return

	def test_check_attributes_string(self):
		self.assertEqual(str, type(self.my_user.first_name))
		self.assertEqual(str, type(self.my_user.last_name))
		self.assertEqual(str, type(self.my_user.email))
		self.assertEqual(str, type(self.my_user.password))
	
	def test_check_attributes_present(self):
		attributes = ["email", "id", "created_at", "updated_at",
		"password", "first_name", "last_name"]
		for attribute in attributes:
		self.assertIn(attribute, self.my_user.__dict__)

	def test_check_func(self):
		"""cheking if User has Docstring"""
		self.assertIsNotNone(User.__doc__)

	def test_check_subclass(self):
		"""checking for subclass in the Supper class"""
		self.assertTrue(issubclass(self.my_user.__class__, BaseModel))

	def test_save(self):
		self.my_user.save()
		self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

	def test_to_dict(self):
		self.assertTrue(hasattr(self.my_user, "to_dict")
	
if __name__ == "__main__":
    unittest.main()
