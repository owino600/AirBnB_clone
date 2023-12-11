#!/usr/bin/python3
from models.base_model import BaseModel
from typing import List
class place(BaseModel):
    """
    city_id (str): name of city
    user_id (str): user id
    name (str): name for place
    description (str): place description
    number_rooms (int): room numbers in the place
    number_bathrooms (int): number of bathrooms in the place
    max_guest (int): number of guests in the place
    price_by_night (int): the price to be paid
    latitude (float): latitude of place
    longitude (float): longitude of place
    amenity_ids (str): list of ammenity_ids
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids: List[str] = []
