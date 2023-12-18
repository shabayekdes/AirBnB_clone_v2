#!/usr/bin/env python3
"""
Unit tests for console.py
Unittest classes:
    Test_console_prompt
    Test_console_exit
    Test_console_help
    Test_console_create
    Test_console_show
    Test_console_destroy
    Test_console_all
    Test_console_update
    Test_console_count
    """

from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch
from models import storage


class Test_console_prompt(unittest.TestCase):
    """test prompting of the command interpreter"""
    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_ine(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

    def test_exit_exit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            pass

    def test_exit_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            pass

class Test_Console_help(unittest.TestCase):
    """test help command"""
    def test_help_quit(self):
        help = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_EOF(self):
        help = "End Of File command to exit the program."
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_create(self):
        help = "Create a new instance of a specified class."
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_all(self):
        help = ("Prints all string representation of all instances\n        "
                "based or not on the class name.")
        
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_show(self):
        help = "Print the string representation of an instance."

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_destroy(self):
        help = ("Deletes an instance based on the class name and id.")
        
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_count(self):
        help = "Count the number of instances of a class."

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help(self):
        help = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
