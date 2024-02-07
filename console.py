#!/usr/bin/python3
"""Building a command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB console
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program."""
        raise SystemExit

    def do_EOF(self, line):
        """Exit with Ctrl+D"""
        return True

    def do_help(self, line):
        """
        Get help on commands.
        Usage: help <command>
        """
        cmd.Cmd.do_help(self, line)

    def emptyline(self):
        """ Do nothing on empty input lines."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
