#!/usr/bin/pythom3

from models.base_model import BaseModel
class Review(BaseModel):

    """
    place_id (str): place id
    user_id (str): user id
    text (str): review text
    """
    place_id = ""
    user_id = ""
    text = ""
