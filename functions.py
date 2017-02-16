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
Base = declarative_base()
engine = create_engine("sqlite:///C:/Users/Shera/Desktop/pomodoro/pomodorotimer.db")
session = sessionmaker(bind=engine)
new_session = session()

#class for manupilating the pomodoro db

class Timer:

	def __init__(self):
		con = new_session.query(Config).first()
		self.duration=con.duration
		self.short_break= con.short_break
		self.long_break = con.long_break
		self.sound_mode = con.sound_mode
		

#Add task name and date
	def getTimer(self,task_name):

		
		duration = self.duration
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
			
#Sets duration for the timer
	def setDuration(self, duration):
		self.duration = duration
		addcommand = update(Config).where(Config.id==1).values(duration=self.duration)
		new_session.execute(addcommand)
		new_session.commit()
		print("You have changed the duration to " + str(self.duration) + " seconds ")

	def setLongbreak(self, long_break):#sets long break for the timer
		self.long_break = long_break
		addcommand = update(Config).where(Config.id==1).values(long_break=self.long_break)
		new_session.execute(addcommand)
		new_session.commit()
		print("Long break " + str(self.long_break) + "seconds")

	def setShortbreak(self, short_break):#sets short break for the timer
		self.short_break = short_break
		addcommand = update(Config).where(Config.id==1).values(short_break=self.short_break)
		new_session.execute(addcommand)
		new_session.commit()
		print("Short break " + str(self.short_break) + "seconds")
	def setSound(self, sound):#sets sound for the timer
		self.sound = sound
		addcommand = update(Config).where(Config.id==1).values(sound=self.sound)
		new_session.execute(addcommand)
		new_session.commit()
		print("Sound has been turned on"+ str(self.sound) + ".")
	 

	



