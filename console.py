#!/usr/bin/python3
""" Console Class"""
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd


class HBNBCommand(cmd.Cmd):
    """Runs the command processers"""
    prompt = "(hbnb)"
    classes = {"BaseModel", "User", "State", "City", "Amenity",
            "Place", "Review"}

    def do_EOF(self, line):
        """shows end of a file"""
        print()
        return True

    def do_quit(self, line):
        """ exits cmd ctrl-D"""
        return True

    def emptyline(self):
        """if the line is empty call emptyline"""
        pass

    def do_create(self, line):
        """Creates a new instance of Class"""
        if len(line) == 0:
            print("** class name missing **")

        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")

        else:
            occurence = eval(line)()
            occurence.save()
            print(occurence.id)

    def do_show(self, line):
        """Prints a string of an instance based on class name and id"""
        store = storage.all()

        if len(line) == 0:
            print("** class name missing **")
            return
        arg = parse(line)
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(arg) < 2:
            print("** instance id missing **")
            return
        read = "{}.{}".format(arg[0], arg[1])

        elif read not in store.keys():
            print("** no instance found **")

        else:
            print(store[read])

    def do_destroy(self, line):
        """delets instance based on class and id"""
        store = storage.all()

        if len(line) == 0:
            print(" ** class name missing **")
            return
        arg = parse(line)

        elif arg[0] not in HBNBCommand.classes:
            print ("** class doesn't exist **")
            return

        elif len(line) < 2:
            print("** instance id missing **")
            return
        read = "{}.{}".format(arg[0], arg[1])

        elif read not in store.keys():
            print("** no instance found **")

        else:
            del store[read]
            storage.save()

    def do_all(self, line):
        """Prints all instances based or not on the class name"""
        arg = parse(line)
        newlist = []
        store = storage.all()

        if len(line) == 0:
            for i in store.values():
                newlist.append(i)
                print(newlist)

        elif arg[0] in HBNBCommand.classes:
            for k, i in store.items():
                if arg[0] in k:
                    newlist.append(i)
                    print(newlist)
                else:
                    print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        arg = parse(line)
        store = storage.all()

        if len(line) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif ("{}.{}".format(arg[0], arg[1])) not in store.key():
            print("** no instance found **")
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return
        elif len(arg) >= 4:
            key = f"{arg[0]}.{arg[1]}"
            check = type(eval(value))
            value = value.strip('"').strip("'")
            setattr(store[key], arg[2], check(value))
            store[key].save()

    def do_count(self, line):
        """count the number of instances"""
        store = storage.all()

        if line in HBNBCommand.classes:
            count = dict(store).keys().count(line)
            print(count)

    def do_parse(line):
        """parses the command entered"""
        return tuple(line.split())

if __name__ == "__main__":
    HBNBCommand().cmdloop()
