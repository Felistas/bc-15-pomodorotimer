## POMODORO TIMER 

This timer uses a technique that break down work into intervals by convention, 25 minutes of break separated short breaks.

## Installation

Clone the repo:

```
https://github.com/Felistas/bc-15-pomodorotimer/tree/develop
```
Navigate to the bc-15-pomodorotimer directory:

```
 $cd bc-15-pomodorotimer 
```

Create virtual environment and activate it

Install the packages

``` 
pip install -r requirements.txt 
```
### Usage 
Run `python pomodoro.py ` to launch the app

A welcome screen as shown below will be displayed

``` Usage:
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
```
### Commands Description
` start <task_title>` - Allows the user to start a task and sets the timer to it's default time i.e Sets the duration to 25 minutes, short break 5 minutes and long break to 15 minutes.

`config_time <duration_in_seconds>`, `config_short_break <duration_in_seconds>`, `<config_long_break <duration_in_seconds>` - Allows the user to specify his/her duration,long break and short break.

`<config_sound>` - Allows the user to turn off the sound

`<config_stop>` - Allows the user to stop the timer 

`<config_reset>` - Allows the user to reset the timer back to its default.







 
