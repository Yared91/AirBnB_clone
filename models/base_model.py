#!/usr/bin/python3
"""BaseModel Class"""
from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel is the super of all the inherited classes.
    arguments:
    id: that assigns unique id
    created_at: time of account creation
    updated_at: time of account update
    __init__: initialization
    __str__: styles string
    __save(self)
    __to_dict(self)
    *args: won't be used
    **kwargs: dictionary
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new Base id."""
        time_style = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.__dict__[key] = datetime.strptime(value, time_style)
                elif "updated_at" == key:
                    self.__dict__[key] = datetime.strptime(value, time_style)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints styles string."""

        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary containing all keys/values."""

        new_dict = {
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "__class__": self.__class__.__name__
                }
        return new_dict
