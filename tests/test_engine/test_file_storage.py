#!/usr/bin/python3
"""Unittest for FileStorage"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import unittest
import os
import json
import models
import pep8


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
        self.assertEquall(py.total_errors, 0, "fix pep8")

    def test_all(self):
        """testes if it returns the dictonary"""
        storage = FileStorage()
        dict_inst = storage.all()
        self.assertTrue(dict_inst is not None)
        self.assertIsInstance(dict_inst, dict)
        self.assertTrue(dict_inst is storage._FileStorage__objects)

    def test_new(self):
        """testing if can set the object to the dict"""
        storages = FileStorage()
        dict_insts = storage.all()
        customer = User()
        customer.id = 56784
        customer.name = "Yared"
        key = f"{customer.__class__.__name__}.{str(customer.id)}"
        self.assertIsNotNone(dict_insts.get(key))

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
        self.assetIs(jstorage.reload(), None)

    def test_errorhandler_reload(self):
        """test if it handles the Error in reload"""
        self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_save(self):
        model_to_test = [BaseModel(), User(), State(), Place(),
                         City(), Amenity(), Review()]

        for model in model_to_test:
            models.storage.new(model)
            models.storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
        for model in models_to_test:
            self.assertIn(model.__class__.__name__ + "." + model.id, save_text)

    def test_save_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)   


if __name__ == "__main__":
    unittest.main()
