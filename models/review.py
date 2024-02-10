#!/usr/bin/python3
"""Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Attributes:
    place_id: ID of the Place
    user_id: Id of User
    text: review of place
    """

    place_id = ""
    user_id = ""
    text = ""
