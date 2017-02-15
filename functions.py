import time
import datetime
import modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules import Task
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine("sqlite:///C:/Users/Shera/Desktop/pomodoro/pomodorotimer.db")
session = sessionmaker(bind=engine)
new_session = session()

#class for manupilating the pomodoro db
class Timer:
	def __init__(self, long_break=0,short_break=0,time=0,sound_mode='',duration=5):
		self.long_break = long_break
		self.short_break = short_break
		self.time = time
		self.sound_mode = sound_mode
		self.duration = duration

#Add task name and date
	def getTimer(self,task_name):
		
		duration = self.duration
		task=Task(name=task_name,date=datetime.now())
		new_session.add(task)
		new_session.commit()
		Base.metadata.create_all(engine)
		start = time.time()
		time.clock()    
		elapsed = 0
		while elapsed < duration:
			time.sleep(1) 
			elapsed = elapsed + 1
			m, s = divmod(duration, 60)
			h, m = divmod(m, 60)
			print ("%d:%02d:%02d" % (h, m, s))


# ('seconds')


