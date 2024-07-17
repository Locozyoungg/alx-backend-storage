#!/usr/bin/env python3
"""
Main file
"""
from exercise import Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

# Additional test cases for get_str and get_int
data_str = "hello"
data_int = 42

key_str = cache.store(data_str)
key_int = cache.store(data_int)

assert cache.get_str(key_str) == data_str
assert cache.get_int(key_int) == data_int