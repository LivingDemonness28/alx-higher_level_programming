#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Represents a Base model for all
    other classes in the project.

    Private Class Attributes:
        __nb_object (int): Num of instantiated bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base.

        Args:
            id (int): Identity of new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON serialization of list of dicts.

        Args:
            list_dictionaries (list): List of dictionaries.
        """
        if (not list_dictionaries):
            return ("[]")
        return (json.dumps(list_dictionaries))
