import time
import datetime
import sys
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

Base = declarative_base()
engine = create_engine("sqlite:///C:/Users/Shera/Desktop/pomodoro/pomodorotimer.db")
session = sessionmaker(bind=engine)
new_session = session()

#class for manupilating the pomodoro db

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


#Add task name and date
	def getTimer(self,task_name):

		
		duration = int(self.duration)
		task=Task(name=task_name,date=datetime.now())
		new_session.add(task)
		new_session.commit()
		Base.metadata.create_all(engine)
		start = time.time()
		time.clock()	
		elapsed = duration
		while elapsed > 0:
			sys.stdout.write ("\r" + str(elapsed))
			time.sleep(1) 
			sys.stdout.flush()
			elapsed = elapsed - 1
			m, s = divmod(duration, 60)
			h, m = divmod(m, 60)
		print(elapsed)
		self.no_of_breaks = self.no_of_breaks + 1
		if self.sound_mode == "on":
			self.sound.play()
		self.breaktimer()



			
#Sets duration for the timer
	def setDuration(self, duration):
		self.duration = duration
		addcommand = new_session.query(Config).order_by(Config.id.desc()).first()
		addcommand.duration = self.duration
		#addcommand = update(Config).where(Config.id==1).values(duration=self.duration)
		#new_session.execute(addcommand)
		new_session.commit()
		print("You have changed the duration to " + str(self.duration) + " seconds ")

	def setLongbreak(self, long_break):#sets long break for the timer
		self.long_break = long_break
		addcommand = new_session.query(Config).order_by(Config.id.desc()).first()
		addcommand.long_break = self.long_break
		#new_session(addcommand)
		new_session.commit()
		print("Long break " + str(self.long_break) + "seconds")

	def setShortbreak(self, short_break):#sets short break for the timer
		self.short_break = short_break
		addcommand = new_session.query(Config).order_by(Config.id.desc()).first()
		addcommand.short_break = self.short_break
		#new_session.execute(addcommand)
		new_session.commit()
		print("Short break " + str(self.short_break) + "seconds")
	def setSound(self, sound_mode):
		self.sound_mode=sound_mode
	#sets sound for the timer
		if sound_mode == "on":
			self.sound.play()
		if sound_mode=="on" or sound_mode=="off":
			addcommand = new_session.query(Config).order_by(Config.id.desc()).first()
			addcommand.sound = sound_mode
		#new_session.execute(addcommand)
			new_session.commit()
			print("Sound has been turned "+ str(sound_mode) + ".")
		else:
			print("Invalid choice")
	def setReset(self):#resets the timer to its default
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

		
		if self.no_of_breaks < 4:
			self.breakduration = self.short_break
			
		else:
			self.no_of_breaks = 0
			self.breakduration = self.long_break
		start = time.time()
		time.clock() 
		elapsed = int(self.breakduration)
		while elapsed > 0:
			#.setSound()
			sys.stdout.write ("\r" + str(elapsed))
			time.sleep(1) 
			sys.stdout.flush()
			elapsed = elapsed - 1
			m, s = divmod(elapsed,60)
			h, m = divmod(m, 60)
		
		print("You can start a new task")
	def listtasks(self):
		tasklist = new_session.query(Task)
		lists = tasklist.all()
		table = []
		for task in lists:
			table.append([str(task.id),str(task.name),str(task.date)])
		print(colored(tabulate(table, headers=["TASK ID","NAME","DATE"], tablefmt='fancy_grid'), 'cyan' ))

		





		
	



