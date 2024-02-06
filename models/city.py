#!/usr/bin/python3
"""City Class"""
from models.base_model import BaseModel


class City(BaseModel):
	"""
		Attributes:
                state_id(str): unique id of the state
		name: Name of the city 
	"""
	state_id = ""
	name = ""

