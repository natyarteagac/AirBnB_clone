#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb)'
    class_name = ["BaseModel"]

    def do_EOF(self, line):
        "exit the program"
        return True

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        "an empty line + ENTER shouldn’t execute anything"
        return cmd.Cmd.postloop(self)

    def do_create(self, arg):
        """ Creating a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        else:
            new_inst = BaseModel()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = "{}.{}".format(args[0], args[1])
            aux = storage.all()
            if obj in aux:
                print(aux[obj])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
