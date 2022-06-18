from sqlalchemy import create_engine
#thisi is were espicify where our thata base is gona be the type(sql,postgres) of database
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

#create database engine 
engine = create_engine('sqlite:///todo.db')

Base = declarative_base()

sessionLocal = sessionmaker(bind=engine, expire_on_commit=False)