#!/usr/bin/python3
"""
Model file storage
"""
import json
from models.base_model import BaseModel
from models.user import User
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return dictionary rep of all objects
        """
        return self.__objects
    def new(self, object):
        """
        set in object wit key <object class name>.id
        """
        self.__object[object.__class__.__name__+ '.' + str(object)] = object
