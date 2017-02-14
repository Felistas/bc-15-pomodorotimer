import time
import datetime
#create your class here then add the timer method to it.
class Timer:
	def __init__(self, long_break,short_break,time,sund_mode,duration):
		self.long_break = long_break
		self.short_break = short_break
		self.time = time
		self.sound_mode = sound_mode
		self.duration = duration
	long_break=0
	short_break=0
	time=0
	sound_mode=''
	duration=0

def getTimer(seconds):
	
	start = time.time()
	time.clock()    
	elapsed = 0
	while elapsed < 10:
		time.sleep(1) 
		elapsed +1

getTimer('seconds')