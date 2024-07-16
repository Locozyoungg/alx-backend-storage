#!/usr/bin/env python3
"""11-schools_by_topic.py"""

from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    :param mongo_collection: A pymongo collection object.
    :param topic: The topic to search for.
    :return: List of schools with the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
