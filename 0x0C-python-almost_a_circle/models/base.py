#!/usr/bin/python3
"""This module contains a base class"""

import json

class Base:
    """Base class for all class created"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
       """ writes the JSON string representation of list_objs to a file"""
       filename = cls.__name__+".json"
       with open(filename, "w") as jsonfile:
           if list_objs is None:
               jsonfile.write("[]")
           else:
               list_dicts = [o.to_dictionary() for o in list_objs]
               jsonfile.write(Base.to_json_string(list_objs))
    
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name = 'Rectangle':
            dummy = cls(1, 1)

        elif cls.__name = 'square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
