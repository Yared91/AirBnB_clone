AirBnB_clone

Introduction
This is the first AirBnB_clone project. In this repository holds one super class BaseModel and subclasses that inherit from it.
we created a console that handles and executes the cmd(line-oriented command processors).
with several methods that can be overridden as hooks for taking actions or altering the base class behaviour.
such as:
do_create - creates new instances
do_show - displays the instances created
do_destroy - deletes an instance based on classname and id
do_all - prints instances regardless based on classname or not
do_update - updates instances based on classname and id

How the cmd works:
Example:

import cmd


class GreetPerson(cmd.Cmd):
  def dO_greet(self, person):
    """greet [person] Greet the name person"""
    if person:
      print("hi", person)
    else:
      pirnt("hi")
  def do_EOF(self, line):
    return True
  def postloop(self):
    print()


if __name__ == '__main__':
  GreetPerson().cmdloop()

In the above example if the user enters greet Yared, the interpreter class includes a method do_greet()
it is called with "Yared" as only argument.
if you give an  argument the output will be personalized, argument is optional to the command.
