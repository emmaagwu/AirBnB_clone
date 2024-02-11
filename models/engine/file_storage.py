#!/usr/bin/env python3
""" Defines the FileStorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON file to instances
   
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """ Returns the dictionary """
        return FileStorage.__objects
   
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        objkey = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[objkey] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        compactdict = FileStorage.__objects
        expandeddict = {key: value.to_dict() for key, value in compactdict.items()}
        with open(FileStorage.__file_path, "w") as jsonfile:
            json.dump(expandeddict, jsonfile)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) """
        try:
            with open(FileStorage.__file_path, "r") as jsonfile:
                expandeddict = json.load(jsonfile)
            for key, value in expandeddict.items():
               classname = key.split('.')[0]
               del value["__class__"]
               self.new(eval(classname)(**value))
        except FileNotFoundError:
            return
