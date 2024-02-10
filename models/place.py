#!/usr/bin/python3
"""Place Class"""
import BaseModel


class Place(BaseModel):
    """
    Attributes:
    city_id: ID of City
    user_id: ID of User
    name: Name of the Place
    description: Description of Place
    number_rooms: Number Room
    number_bathrooms: Number of Bathrooms
    max_guest: Max Guests
    price_by_night: Price of place for a night
    latitude: Location of place in latitude
    longitude: Location of place in longituted
    amenity_ids: IDs of Amenitys list
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
