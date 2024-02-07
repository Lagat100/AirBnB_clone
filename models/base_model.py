#!/usr/bin/python3
"""BaseModel module, Parent class for all classes"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel class - template for all other classes"""
    def __init__(self, *args, **kwargs):
        """Initialize attributes: random uuid, dates created/updated
        """
        if kwargs:
            for key, val, in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints a string rep of class name, id, and dictionary"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates instance 'updated_at' with updated time and saves to a serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dict with string formats of times;add class info to dict
        """
        dict = {}
        dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dict[k] = v.isoformat()
            else:
                dict[k] = v
        return dict
