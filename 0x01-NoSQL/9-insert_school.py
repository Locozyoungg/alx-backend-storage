#!/usr/bin/env python3
"""9-insert_school.py"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    :param mongo_collection: A pymongo collection object.
    :param kwargs: The key-value pairs to be inserted as a document.
    :return: The new document's _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
