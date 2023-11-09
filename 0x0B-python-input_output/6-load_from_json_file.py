#!/usr/bin/python3
"""Defines JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create Python object from JSON file."""
    with open(filename) as file:
        return (json.load(file))
