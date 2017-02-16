"""
Usage:
    pomodoro start <task_title>
    pomodoro config_time <duration_in_seconds>
    pomodoro config_short_break <duration_in_seconds>
    pomodoro config_long_break <duration_in_seconds>
    pomodoro config_sound <state>
    pomodoro stop
    pomodoro list
    pomodoro reset 
    pomodoro (-i | --interactive)
    pomodoro (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""


import sys
import cmd
import os
from docopt import docopt, DocoptExit
from functions import Timer
from colorama import init 
from pyfiglet import Figlet
from termcolor import *

init()
font = Figlet(font='poison')
introduction = font.renderText('POMODORO')
os.system('clear')
cprint(introduction, "yellow", attrs=['blink'])



def docopt_cmd(func):
    
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Pomodoro (cmd.Cmd):
    #intro = 'Welcome to pomodoro timer!' \
        #+ ' (type help for a list of commands.)'
    print(colored(__doc__,'green'))
    prompt = 'Enter command>>'
    file = None
    new_timer=Timer()

    @docopt_cmd
    def do_start(self, arg):
        """Usage: start <task_title>"""
        try:
            self.new_timer.getTimer(arg['<task_title>'])
            print("Task successfully added")
        except ValueError:
            print("Invalid value entered")
            return
        except:
            pass
       

    @docopt_cmd
    def do_config_time(self, arg):
        """Usage: config_time <duration_in_seconds>"""
        try:
            duration = int(arg['<duration_in_seconds>'])
        except ValueError:
            print(colored("Invalid value entered", 'red'))
            return
        self.new_timer.setDuration(arg['<duration_in_seconds>'])

    def do_config_long_break(self, duration_in_seconds):
        """Usage: config_long_break <duration_in_seconds>"""
        try:
            long_time_break = int(duration_in_seconds)
        except ValueError:
            print(colored("Invalid input", 'red'))
            return 
            
        self.new_timer.setLongbreak(duration_in_seconds)
        
        
    def do_config_short_break(self, duration_in_seconds):
        """Usage: config_short_break <duration_in_seconds>"""
        try:
            short_time_break = int(duration_in_seconds)
        except ValueError:
            print(colored("Invalid Input",'red'))
            return

        self.new_timer.setShortbreak(duration_in_seconds)
        
        
    def do_config_sound(self, arg):
        """Usage: config_sound <state>"""
        if arg.upper() not in ['ON','OFF']:
            print(colored("State should be on or off", 'red'))
            return
        self.new_timer.setSound(arg.lower())
        
    def do_reset(self, arg):
        self.new_timer.setReset()
        print(colored("You have reset to default", 'yellow'))
   
    def do_list(self, arg):
        self.new_timer.listtasks()


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


if __name__ == '__main__':
    try:
        Pomodoro().cmdloop()
    except KeyboardInterrupt:
        Pomodoro().cmdloop()
