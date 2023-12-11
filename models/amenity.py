#!/usr/bin/python3
from models.base_model import BaseModel
class Amenity(BaseModel):
    """
    attribute:
    name (str): name of ammenity
    """
    name: str = ""
