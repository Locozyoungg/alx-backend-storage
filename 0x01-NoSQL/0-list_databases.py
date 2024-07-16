#!/usr/bin/env python3
"""
This script lists all databases in MongoDB.
"""

from pymongo import MongoClient

def list_databases():
    """
    List all databases in MongoDB.
    """
    client = MongoClient('localhost', 27017)
    return client.list_database_names()

if __name__ == "__main__":
    databases = list_databases()
    for db in databases:
        print(db)
        