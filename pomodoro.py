"""
Usage:
    pomodoro start <task_title>
    pomodoro config_time <duration_in_minutes>
    pomodoro config short_break <duration_in_minutes>
    pomodoro config long_break <duration_in_minutes>
    pomodoro config sound <state>
    pomodoro stop
    pomodoro list
    pomodoro (-i | --interactive)
    pomodoro (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""


import sys
import cmd
from docopt import docopt, DocoptExit
from functions import Timer


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
    print(__doc__)
    prompt = 'Enter command>>'
    file = None

    @docopt_cmd
    def do_start(self, arg):
       """Usage: start <task_title>"""
       timer = Timer()
       timer.getTimer(arg['<task_title>'])
       print("Task successfully added")
       

    @docopt_cmd
    def do_config_time(self, arg):
        """Usage: config_time <duration_in_minutes>"""
        new_timer=Timer()
        new_timer.setDuration(arg['<duration_in_minutes>'])
        print("Changed the duration successfully")
 

        
    def do_config_shortbreak(self, arg):
 

        print(arg)
    def do_config_long_break(self, arg):
 

        print(arg)
    def do_config_sound(self, arg):


        print(arg)
    def do_stop(self, arg):


        print(arg)
    def do_list(self, arg):
  

        print(arg)


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


if __name__ == '__main__':
    try:
        Pomodoro().cmdloop()
    except KeyboardInterrupt:
        print("\nff")
        exit()
