#!usr/bin/python3

'''city module'''

from models.base_model import BaseModel


class City(BaseModel):
    '''City class'''
    state_id = ''  # stores state id (foreingkey)
    name = ''
