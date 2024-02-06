#!/usr/bin/python3
"""BaseModel module"""
import uuid
import datetime


class BaseModel:
    """BaseModel class - template for all other classes"""
    def __init__(self, id, created_at, updated_at):
        self.id = string(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[BaseModel] ({self.id}) {<self.__dict__>}"

    def save(self):

