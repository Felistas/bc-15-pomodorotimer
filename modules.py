
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
engine = create_engine("sqlite:///tasks.db")
#define columns for the table named tasks
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
	




Base.metadata.create_all(engine)