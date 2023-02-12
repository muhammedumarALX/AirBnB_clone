#!/usr/bin/python3
import uuid
from datetime import datetime
"""This module defines a class `BaseModel`"""


class BaseModel():
    """defines all common attributes/methods for other class"""

    def __init__(self, *args, **kwargs):
        '''Initializes a new instance of BaseModel

        Args:
            *args (any): unsused
            **kwargs (dict): key & value pair of attributes
        '''

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "update_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''returns class name, id and attribute dictionary
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates last update time `updated_at`
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''`__dicy__`creates a new dictionary, adding a key and returning
        datetimes converted to strings
        '''
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
