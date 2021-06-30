#!/usr/bin/python3
"""
Contains the entry point of the command interpreter


"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """

    prompt = '(hbnb) '
    class_name = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

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
        """
        Prints the string representation of
        an instance based on the class name and id
        """
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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
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
                del aux[obj]
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        args = arg.split()
        l_obj = []
        aux = storage.all()
        if len(args) == 0:
            for key, value in aux.items():
                l_obj.append(str(value))
            print(l_obj)
        elif args[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        else:
            for key, value in aux.items():
                if key.split(".")[0] == args[0]:
                    l_obj.append(str(value))
            print(l_obj)

    def do_update(self, arg):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)
        """
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
            print(obj)
            if obj not in aux:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                trimp = args[3]
                trimp = trimp[1:-1]
                up_obj = aux.get(obj)
                setattr(up_obj, args[2], trimp)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
