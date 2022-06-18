from asyncio import Task
from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))