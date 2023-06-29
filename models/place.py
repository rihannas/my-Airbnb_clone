#!usr/bin/python3

'''place module'''

from models.base_model import BaseModel


class Place(BaseModel):
    '''Place class'''
    city_id = ''  # stores city id (foreingkey)
    user_id = ''  # store user id (foreingkey)
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # this list will contain list of Amenity.id
