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
            self.commands.onecmd("\n")
            self.assertEqual(output.getvalue(), '')

    def test_create(self):
        """testing the create command"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.commands.onecmd('create')
            self.assertEqual("** class name missing **\n", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.commands.onecmd('create MyClass')
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_show(self):
        """testing the show command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("MyClass.show()")
            self.assertEqual("** class doesn't exist **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show foo")
            self.assertEqual("** instance id missing **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.show('456')")
            self.assertEqual("** no instance found **", output.getvalue())

    def test_destroy(self):
        """testing the destroy command"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("destroy")
            self.assertEqual("** class name missing **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("destroy BaseModel 121212")
            self.assertEqual("** no instance found **", output.getvalue())

    def test_all(self):
        """testing the all command"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("all BaseModel")
            self.assertEqual("[]", output.getvalue())

    def test_update(self):
        """testing the update command"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("update")
            self.assertEqual("** class name missing **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("update MyModel")
            self.assertEqual("** class doesn't exist **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("update BaseModel 121212")
            self.assertEqual("** no instance found **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("update BaseModel existing-id")
            self.assertEqual("** attribute name missing **", output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            self.typing.onecmd("update BaseModel existing-id first_name")
            self.assertEqual("** value missing **", output.getvalue())

    def test_docstring(self):
        """tests if console has docstring"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_cmd(self):
        """tests cmd output"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.commands.onecmd("User.count()")
            self.assertEqual(type(eval(output.getvalue())), int)


if __name__ == '__main__':
    unittest.main()
