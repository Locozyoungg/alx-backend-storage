#!/usr/bin/env python3
"""12-log_stats.py"""

from pymongo import MongoClient

def log_stats():
    """Provides statistics about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    get_logs = collection.count_documents({"method": "GET"})
    post_logs = collection.count_documents({"method": "POST"})
    put_logs = collection.count_documents({"method": "PUT"})
    patch_logs = collection.count_documents({"method": "PATCH"})
    delete_logs = collection.count_documents({"method": "DELETE"})
    status_check_logs = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_logs}")
    print(f"\tmethod POST: {post_logs}")
    print(f"\tmethod PUT: {put_logs}")
    print(f"\tmethod PATCH: {patch_logs}")
    print(f"\tmethod DELETE: {delete_logs}")
    print(f"{status_check_logs} status check")

if __name__ == "__main__":
    log_stats()
