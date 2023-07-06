#!usr/bin/python3

'''city module'''

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    '''City class'''
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)  # stores state id (foreingkey)
    name = Column(String(60), nullable=False)
