#!/usr/bin/python3
""" Console Class"""
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
    """Runs the command processors"""
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
        """if the line is empty call empty line"""
        pass

    def do_create(self, line):
        """Creates a new instance of Class"""
        if len(line) == 0:
            print("** class name missing **")

        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")

        else:
            occurrence = eval(line)()
            occurrence.save()
            print(occurrence.id)

    def do_show(self, line):
        """Prints a string of an instance based on class name and id"""
        store = storage.all()

        if len(line) == 0:
            print("** class name missing **")
            return
        arg = parse(line)
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif len(arg) < 2:
            print("** instance id missing **")
            return
        read = "{}.{}".format(arg[0], arg[1])

        if read not in store.keys():
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

        if arg[0] not in HBNBCommand.classes:
            print ("** class doesn't exist **")
            return

        elif len(line) < 2:
            print("** instance id missing **")
            return
        read = "{}.{}".format(arg[0], arg[1])

        if read not in store.keys():
            print("** no instance found **")

        else:
            del store[read]
            storage.save()

    def do_all(self, line):
        """Prints all instances based or not on the class name"""
        arg = parse(line)
        new_list = []
        store = storage.all()

        if len(line) == 0:
            for i in store.values():
                new_list.append(i)
                print(new_list)

        elif arg[0] in HBNBCommand.classes:
            for k, i in store.items():
                if arg[0] in k:
                    new_list.append(i)
                    print(new_list)
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
            check = type(eval(arg[3]))
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

    def default(self, line):
        """handles errors and runs previous commands"""
        arg = line.split('.')
        subarg = arg[0]

        if len(arg) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            arg = arg[1].split('(')
            cmds = arg[0]

            command_mapping = {
                    'all': HBNBCommand.do_all,
                    'count': HBNBCommand.do_count,
                    'show': HBNBCommand.do_show,
                    'destroy': HBNBCommand.do_destroy,
                    'update': HBNBCommand.do_update
                    }
            if cmds in command_mapping:
                if cmds == 'show' or cmds == 'destroy':
                    arg = arg[1].split(')')
                    num = arg[0].strip("'").strip('"')
                    arg = subarg + ' ' + num
                    command_mapping[cmds](self, arg)
                elif cmds == 'update':
                    arg = arg[1].split(',')
                    num = arg[0].strip("'").strip('"')
                    name1 = arg[1].strip()
                    name2 = arg[2].strip().strip(')')
                    arg = subarg + ' ' + num + ' ' + name1 + ' ' + name2
                    command_mapping[cmds](self, arg)
                else:
                    command_mapping[cmds](self, subarg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
