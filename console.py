#!/usr/bin/python3
"""
Contains the entry
point of the
command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Our command interpreter
    """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        return cmd.Cmd.postloop(self)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
