#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseMode):

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)