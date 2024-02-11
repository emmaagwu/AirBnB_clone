#!/usr/bin/env python3
""" Defines the command interpreter """
import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage
import re
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """ This is the entry point of the command interpreter """

    prompt = "(hbnb) "
    __appclasses = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        createArgs = parse(arg)
        if len(createArgs) == 0:
            print("** class name missing **")
            return
        elif createArgs[0] not in HBNBCommand.__appclasses:
            print("** class doesn't exist **")
        else:
            newModel = eval(createArgs[0])()
            print(newModel.id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        showArgs = parse(arg)
        if len(showArgs) == 0:
            print("** class name missing **")
            return
        elif showArgs[0] not in HBNBCommand.__appclasses:
            print("** class doesn't exist **")
            return
        elif len(showArgs) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(showArgs[0], showArgs[1]) not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(showArgs[0], showArgs[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        showArgs = parse(arg)
        objdic = storage.all()
        if len(showArgs) == 0:
            print("** class name missing **")
            return
        elif showArgs[0] not in HBNBCommand.__appclasses:
            print("** class doesn't exist **")
            return
        elif len(showArgs) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(showArgs[0], showArgs[1]) not in objdic.keys():
            print("** no instance found **")
        else:
            del(objdic["{}.{}".format(showArgs[0], showArgs[1])])
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argu = parse(arg)
        if len(argu) > 0 and argu[0] not in HBNBCommand.__appclasses:
            print("** class doesn't exist **")
        else:
            objlist = []
            for obj in storage.all().values():
                if len(argu) > 0 and argu[0] == obj.__class__.__name__:
                    objlist.append(obj.__str__())
                elif len(argu) == 0:
                    objlist.append(obj.__str__())
                print(objlist)

    def do_update(self, arg):
        """ Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argu = parse(arg)
        if len(argu) == 0:
            print("** class name missing **")
            return False
        if argu[0] not in HBNBCommand.__appclasses:
            print("** class doesn't exist **")
            return False
        if len(argu) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argu[0], argu[1]) not in storage.all().keys():
            print("** no instance found **")
            return False
        if len(argu) == 2:
            print("** attribute name missing **")
        if len(argu) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argu) == 4:
            obj = storage.all()["{}.{}".format(argu[0], argu[1])]
            if argu[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argu[2]])
                obj.__dict__[argu[2]] = valtype(argu[3])
            else:
                obj.__dict__[argu[2]] = argu[3]
        elif type(eval(argu[2])) == dict:
            obj = storage.all()["{}.{}".format(argu[0], argu[1])]
            for k, v in eval(argu[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
