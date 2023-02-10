#!/usr/bin/python3
'''Contains the entry point of the command interpreter.'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Command line-interpreter.'''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''To exit the program.'''
        return True

    def do_EOF(self, arg):
        '''EOF signal to exit a program.'''
        return True

    def emptyline(self):
        '''For an emptyline.'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
