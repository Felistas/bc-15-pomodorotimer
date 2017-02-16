
import time
import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from sqlalchemy import create_engine, MetaData, Table

Base = declarative_base()
engine = create_engine("sqlite:///pomodorotimer.db")
#define columns for the table named tasks
duration = 1500
short_break = 300
long_break = 900
mytime = 0
sound_mode = 'on'
class Task(Base):

	__tablename__='tasks'
	id=Column(Integer,primary_key=True,autoincrement=True)
	name=Column(String(50))
	date=Column(DateTime())
class Config(Base):
	__tablename__='configure'
	id=Column(Integer,primary_key=True,autoincrement=True)
	duration=Column(Integer())
	long_break=Column(Integer())
	short_break=Column(Integer())
	sound_mode=Column(String(20))
	




Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
new_session = session()
config = Config(duration=duration,long_break=long_break,short_break=short_break)
new_session.add(config)
new_session.commit()