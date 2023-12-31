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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization of list of objects to file.

        Args:
            list_objs (list): List of inherited Base instances.
        """
        if (list_objs is None):
            list_objs = []
        fn = cls.__name__ + ".json"
        with open(fn, "w") as file:
            json_data = cls.to_json_string([o.to_dictionary()
                                            for o in list_objs])
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """Return deserialization of JSON string.

        Args:
            json_string (str): JSON str representation of list of dicts.
        Returns:
            If json_string is None - an empty list.
            Otherwise - Python list represented by json_string.
        """
        if (not json_string):
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return class instantied from dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs attributes to initialize.
        """
        if (cls.__name__ == "Rectangle"):
            di = cls(1, 1)
        else:
            di = cls(1)

        di.update(**dictionary)
        return (di)

    @classmethod
    def load_from_file(cls):
        """Return list of classes instantiated from
        file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If file doesn't exist - an empty list.
            Otherwise - List of instantiated classes.
        """
        fn = cls.__name__ + ".json"
        try:
            with open(fn, "r") as file:
                jd = file.read()
                dl = cls.from_json_string(jd)
                return ([cls.create(**i) for i in dl])
        except FileNotFoundError:
            return ([])
