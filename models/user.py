#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):

    """
    email (str): user email
    password (str): user password
    first_name (str): firt_name
    last_name (str): last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
