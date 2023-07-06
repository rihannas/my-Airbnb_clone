#!usr/bin/python3

'''state module'''

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''State class'''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, delete")
