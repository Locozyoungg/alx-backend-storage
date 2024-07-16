#!/usr/bin/env python3
"""8-all.py"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    
    :param mongo_collection: A pymongo collection object.
    :return: A list of documents in the collection or an empty list if no documents.
    """
    return list(mongo_collection.find())

