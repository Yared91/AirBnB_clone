#!/usr/bin/python3
"""Unittest for FileStorage"""
import unittest
import os
import json
import models
import pep8
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing the FileStorage and it's attributes"""
    @classmethod
    def setUpClass(cls):
        cls.my_review = Review
        cls.my_review.place_id = "Addis"
        cls.my_review.user_id = "Elilta"
        cls.my_review.text = "First"

    @classmethod
    def tearDownClass(cls):
        del cls.my_review

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_pycodestyle(self):
        """test the pycode style"""
        style = pep8.StyleGuide(quiet=True)
        py = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(py.total_errors, 2, "fix pep8")

    def test_all(self):
        """testes if it returns the dictonary"""
        storages = FileStorage()
        dict_inst = storage.all()
        self.assertTrue(dict_inst is not None)
        self.assertIsInstance(dict_inst, dict)
        self.assertTrue(dict_inst is storage._FileStorage__objects)

    def test_new(self):
        """testing if can set the object to the dict"""
        storages = FileStorage._FileStorage__objects
        dict_insts = dict(storage)
        """creating instance with **kwargs and checks if the object is in __objects"""
        new = BaseModel()
        key = f"{new.__class__.__name__}.{str(new.id)}"
        self.assertEqual(storages.get(key), new)
        self.assertTrue(key not in dict_insts)
        self.assertTrue(key in storages)

    def test_reload(self):
        """testing reloading of obj from string file json"""
        jstorage = FileStorage()
        """removes file if present"""
        try:
            os.remove("file.json")
        except:
            pass
        """Creat a new file"""
        with open ("file.json", "w") as f:
            f.write("{}")
        """Read file and assert its content"""
        with open ("file.json", "r") as r:
            for i in r:
                self.assertEqual(i, "{}")
        """Assert the reload that return None"""
        self.assertIs(jstorage.reload(), None)

    def test_save(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", "w") as f:
            f.write("holder")

        with open("file.json", "r") as f:
            save_text = f.read()
            storage.save()
            new_file = f.read()
        self.assertNotEqual(save_text, new_file)

    def test_save_arg(self):
        with self.assertRaises(TypeError):
            storage.save(None)


if __name__ == "__main__":
    unittest.main()
