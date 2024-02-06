#!/usr/bin/python3
"""for the User class"""
from models.base_model import BaseModel


class User(BaseModel):
	""" for a user

        Attributes:
        email: Email of a user
        password: Password of a user
        first_name: First name of a user
        last_name: Last name of a user.
        """

        email = ""
        password = ""
        first_name = ""
        last_name = ""
