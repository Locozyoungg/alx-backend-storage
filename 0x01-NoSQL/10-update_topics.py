#!/usr/bin/env python3
"""10-update_topics.py"""

from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    :param mongo_collection: A pymongo collection object.
    :param name: The school name to update.
    :param topics: The list of topics to be approached in the school.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
