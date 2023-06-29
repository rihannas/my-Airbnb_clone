#!/usr/bin/python3

'''review module'''

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    '''Review class'''
    place_id = ""  # stores Place.id (foreignkey)
    user_id = ""  # stores User.id (foreignkey)
    text = ""  # the comment the user will write
