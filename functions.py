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
		addtime = update(Config).where(Config.id==1).values(duration=self.duration)
		new_session.execute(addtime)
		new_session.commit()
		print("You have changed the duration to " + str(self.duration) + " seconds ")

	def setLongbreak(self, long_break):
		self.long_break = long_break
		addlongbreak = update(Config).where(Config.id==1).values(long_break=self.long_break)
		new_session.execute(addlongbreak)
		new_session.commit()
		print("Long break " + str(self.long_break) + "seconds")
	



