#!/usr/bin/python3
"""Unittest Console"""
import json
import unittest
import console
import tests
import os
import pep8
import models
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
    @classmethod
    def setUpClass(self):
        """Creates file"""
        self.commands = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Removes file"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_console_pycodestyle(self):
        """test the console pycode style"""
        style = pep8.StyleGuide(quiet=False)
        faults = 0
        faults = faults + style.check_files(['console.py']).total_errors
        self.assertEquall(faults, 0, "fix pep8")

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
        with patch('sys.stdout', new=StringIO()) as output:
            self.commands.onecmd('new User')
            self.commands.onecmd('new User')
            self.commands.onecmd("User.all()")
            self.assertEqual("[[User]", output.getvalue()[0:7])

    def test_show(self):
        """testing the show command"""
        show_result = [
                ("show", "** class name missing **\n"),
                ("MyClass.show()", "** class doesn't exist **\n"),
                ("show foo", "** instance id missing **\n"),
                ("User.show('456')", "** no instance found **\n")
                ]
        with patch('sys.stdout', new=StringIO()) as output:
            for cmds, result in show_result:
                self.commands.onecmd(cmds)
                self.assertEqual(result, output.getvalue())

    def test_destroy(self):
        """testing the destroy command"""
        destroy_result = [
                ("destroy", "** class name missing **\n"),
                ("destroy MyModel", "** class doesn't exist **\n"),
                ("destroy BaseModel", "** instance id missing **\n"),
                ("destroy BaseModel 121212", "** no instance found **\n")
                ]
        with patch('sys.stdout', new=StringIO()) as output:
            for cmds, result in destroy_result:
                self.commands.onecmd(cmds)
                self.assertEqual(result, output.getvalue())

    def test_all(self):
        """testing the all command"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.commands.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())
            self.commands.onecmd("all BaseModel")
            self.assertEqual("[]\n", output.getvalue())

    def test_update(self):
        """testing the update command"""
        update_result = [
                ("update", "** class name missing **\n"),
                ("update MyModel", "** class doesn't exist **\n"),
                ("update BaseModel", "** instance id missing **\n"),
                ("update BaseModel 121212", "** no instance found **\n"),
                ("update BaseModel existing-id",
                    "** attribute name missing ** \n"),
                ("update BaseModel existing-id first_name",
                    "** value missing **\n")
                ]
        with patch('sys.stdout', new=StringIO()) as output:
            for cmds, result in update_result:
                self.commands.onecmd(cmds)
                self.assertEqual(result, output.getvalue())

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
