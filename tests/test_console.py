#!/usr/bin/python3
"""Unittest Console"""
import json
import unittest
import console
import tests
import os
import pep8
import models
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """Testing the Console and its methods"""

    def test_console_pycodestyle(self):
        """test the console pycode style"""
        style = pep8.StyleGuide(quiet=False)
        faults = 0
        faults = faults + style.check_files(['console.py']).total_errors
        self.assertEqual(faults, 1, "fix pep8")

    def test_emptyline(self):
        """tastes when an empty line is entered"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("\n")
            self.assertEqual(output.getvalue(), '')

    def test_create(self):
        """testing the create command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create')
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create MyClass')
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_show(self):
        """testing the show command"""
        prints = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyClass.show()"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show foo"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show('456')"))
            self.assertEqual(prints, output.getvalue().strip())

    def test_destroy(self):
        """testing the destroy command"""
        prints = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 121212"))
            self.assertEqual(prints, output.getvalue().strip())

    def test_all(self):
        """testing the all command"""
        prints = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = ""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertEqual(prints, output.getvalue().strip())

    def test_update(self):
        """testing the update command"""
        prints = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 121212"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** attribute name missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand()
                             .onecmd("update BaseModel existing-id"))
            self.assertEqual(prints, output.getvalue().strip())
        prints = "** value missing **"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel existing-id
                                                  first_name"))
            self.assertEqual(prints, output.getvalue().strip())

    def test_docstring(self):
        """tests if console has docstring"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_cmd(self):
        """tests cmd output"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(type(eval(output.getvalue())), int)


if __name__ == '__main__':
    unittest.main()
