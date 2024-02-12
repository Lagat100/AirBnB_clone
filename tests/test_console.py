#!/usr/bin/python3
""" Unittest for the console"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.temp_stdout = StringIO()

    def tearDown(self):
        self.temp_stdout.close()
        del self.console

    def test_help_command(self):
        with patch('sys.stdout', new=self.temp_stdout):
            self.console.onecmd("help")
            output = self.temp_stdout.getvalue().strip()
            self.assertIn("List available commands", output)

    def test_quit_command(self):
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_create_command(self):
        with patch('sys.stdout', new=self.temp_stdout):
            self.console.onecmd("create BaseModel")
            output = self.temp_stdout.getvalue().strip()
            self.assertTrue(output.isalnum())  # Ensure output is alphanumeric

    def test_show_command(self):
        with patch('sys.stdout', new=self.temp_stdout):
            self.console.onecmd("show BaseModel")
            output = self.temp_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_command(self):
        with patch('sys.stdout', new=self.temp_stdout):
            self.console.onecmd("destroy BaseModel")
            output = self.temp_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_all_command(self):
        with patch('sys.stdout', new=self.temp_stdout):
            self.console.onecmd("all")
            output = self.temp_stdout.getvalue().strip()
            self.assertTrue(output.startswith("["))

    def test_update_command(self):
        with patch('sys.stdout', new=self.temp_stdout):
            self.console.onecmd("update BaseModel")
            output = self.temp_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")


if __name__ == '__main__':
    unittest.main()
