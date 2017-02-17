"""class for manupilating the pomodoro db"""
import time
import datetime
import sys
import os
from modules import Task, Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from modules import Task, Config
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from pygame import mixer
from tabulate import tabulate
from termcolor import colored
from pyfiglet import Figlet
Base = declarative_base()
engine = create_engine("sqlite:///pomodorotimer.db")
session = sessionmaker(bind=engine)
new_session = session()
class Timer:
	def __init__(self):
		con = new_session.query(Config).order_by(Config.id.desc()).first()
		self.duration=con.duration
		self.short_break= con.short_break
		self.long_break = con.long_break
		mixer.init()
		self.sound = mixer.Sound("ding.wav")
		self.sound_mode = con.sound_mode
		self.breakduration = con.short_break
		self.no_of_breaks = 0
	def getTimer(self,task_name):
		"""Add task name and date"""
		duration = int(self.duration)
		task=Task(name=task_name,date=datetime.now())
		new_session.add(task)
		new_session.commit()
		Base.metadata.create_all(engine)
		start = time.time()
		time.clock()	
		elapsed = duration
		output = ''
		font= Figlet(font='standard')
		while elapsed > 0:
			output = str(int(elapsed // 60)) + " min " + str(int(elapsed % 60)) + " sec "
			output = font.renderText(output)
			sys.stdout.write ("\r" + output)
			time.sleep(1) 
			sys.stdout.flush()
			os.system('cls')
			elapsed = elapsed - 1
			m, s = divmod(duration, 60)
			h, m = divmod(m, 60)
		print(colored(font.renderText("Time up"), 'green'))
		self.no_of_breaks = self.no_of_breaks + 1
		if self.sound_mode == "on":
			self.sound.play()
		time.sleep(2)
		os.system('cls')
		self.breaktimer()
	def setDuration(self, duration):
		"""Sets duration for the timer"""
		self.duration = duration
		addcommand = new_session.query(Config).order_by(Config.id.desc()).first()
		addcommand.duration = self.duration
		new_session.commit()
		print(colored("You have changed the duration to " + str(self.duration) + " seconds "), 'yellow')
	def setLongbreak(self, long_break):
		"""sets long break for the timer"""
		self.long_break = long_break
		addcommand = new_session.query(Config).order_by(Config.id.desc()).first()
		addcommand.long_break = self.long_break
		#new_session(addcommand)
		new_session.commit()
		print("Long break " + str(self.long_break) + "seconds")
	def setShortbreak(self, short_break):
		"""sets short break for the timer"""
		self.short_break = short_break
		addcommand = new_session.query(Config).order_by(Config.id.desc()).first()
		addcommand.short_break = self.short_break
		new_session.commit()
		print("Short break " + str(self.short_break) + "seconds")
	def setSound(self, sound_mode):
		"""sets sound for the timer"""
		self.sound_mode=sound_mode
		if sound_mode == "on":
			self.sound.play()
		if sound_mode=="on" or sound_mode=="off":
			addcommand = new_session.query(Config).order_by(Config.id.desc()).first()
			addcommand.sound = sound_mode
			new_session.commit()
			print("Sound has been turned "+ str(sound_mode) + ".")
		else:
			print("Invalid choice")
	def setReset(self):
		"""resets the timer to its default"""
		addcommand = new_session.query(Config).order_by(Config.id.desc()).first()
		addcommand.duration = 1500
		addcommand.long_break = 900
		addcommand.short_break = 300
		addcommand.sound_mode = "on"
		self.sound_mode="on"
		self.duration = 1500
		self.long_break = 900
		self.short_break = 300
		new_session.commit()
	def breaktimer(self):
		"""Sets the number of breaks"""
		if self.no_of_breaks < 4:
			self.breakduration = self.short_break	
		else:
			self.no_of_breaks = 0
			self.breakduration = self.long_break
		start = time.time()
		time.clock() 
		elapsed = int(self.breakduration)
		output = ''
		font= Figlet(font='standard')
		while elapsed > 0:
			output = str(int(elapsed // 60)) + " min " + str(int(elapsed % 60)) + " sec "
			output = font.renderText(output)
			sys.stdout.write ("\r" + output)
			time.sleep(1) 
			sys.stdout.flush()
			os.system('cls')
			elapsed = elapsed - 1
			m, s = divmod(elapsed,60)
			h, m = divmod(m, 60)
		print(colored(font.renderText("Break is over"), 'green'))
		print("You can start a new task")
	def listtasks(self):
		"""Displays the list of tasks"""
		tasklist = new_session.query(Task)
		lists = tasklist.all()
		table = []
		for task in lists:
			table.append([str(task.id),str(task.name),str(task.date)])
		print(colored(tabulate(table, headers=["TASK ID","NAME","DATE"], tablefmt='fancy_grid'), 'cyan' ))


		





		
	


