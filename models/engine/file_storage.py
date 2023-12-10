#!/usr/bin/python3
"""
<<<<<<< HEAD
Module for serializing and deserializing data
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    FileStorage class for storing, serializing and deserializing data
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
         Sets an object in the __objects dictionary with a key of 
         <obj class name>.id.
        """
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj


    def all(self):
        """
        Returns the __objects dictionary. 
        It provides access to all the stored objects.
        """
        return  FileStorage.__objects


    def save(self):
        """
        Serializes the __objects dictionary into 
        JSON format and saves it to the file specified by __file_path.
        """
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        This method deserializes the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
=======
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
>>>>>>> cc6f43e5bb60da5ad50a89585e3e8ba685d67c45
