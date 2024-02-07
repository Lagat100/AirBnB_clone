#!/usr/bin/python3
""" FileStorage module """
import json
import os.path as path
from models.base_model import BaseModel


class FileStorage:
    """serializes and deserializes json files"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns a dictionary of <class>.<id> : object instance"""
        return self.__objects

    def new(self, obj):
        """adds a new obj to existing dictionary of instances"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save obj dictionaries to json file"""
        my_dict = {}

        with open(self.__file_path, mode='w', encoding='UTF-8') as f:
            for key, obj in self.__objects.items():
                """if type(obj) is dict:
                        my_dict[key] = obj
                    else:
                """
                my_dict[key] = obj.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """if json file exists, convert obj dicts bacj to instances"""
        try:
            if path.isfile(self.__file_path):
                with open(self.__file_path, mode='r', encoding='UTF-8') as f:
                    for key, value in json.load(f).items():
                        value = eval(value['__class__'])(**value)
                        self.__objects[key] = value
        except FileNotFoundError:
            pass
