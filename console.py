#!/usr/bin/python3
"""The Command Line Interpreter."""

from models import *
import cmd


class HBNBCommand(cmd.Cmd):
    """Class that defines Airbnb clone public class instances."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Function handle end of file character (Ctrl+D)."""

        print()
        return (True)

    def do_quit(self, line):
        """Function that exits the shell in interactive mode."""

        return (True)

    def emptyline(self):
        """Function that does nothing on ENTER."""

        pass

    def do_create(self, line):
        """Function that creates new instance of BaseModel."""

        if line == "" or line is None:
            print("** class name missing **")

        elif line not in storage.classes():
            print("** class doesn't exist **")

        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance)

    def do_show(self, line):
        """Function that prints the string representation of an instance."""

        if line == "" or line is None:
            print("** class name missing **")

        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(words) < 2:
                print("** instance id missing **")

            else:
                patt = "{}.{}".format(words[0], words[1])
                if patt not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[patt])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
