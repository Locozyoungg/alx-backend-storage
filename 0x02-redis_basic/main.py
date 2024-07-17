#!/usr/bin/env python3
""" Main file """

from exercise import Cache, replay

cache = Cache()

# Test storing different types of data
cache.store("foo")
cache.store("bar")
cache.store(42)

# Replay the history of calls to the store method
replay(cache.store)

# Test case 1: Storing and retrieving binary data
data1 = b"first"
key1 = cache.store(data1)
print(key1)
print(cache.get(key1))

# Test case 2: Counting store method calls
print(cache.get(cache.store.__qualname__))

# Test case 3: Storing and retrieving binary data
data2 = b"second"
key2 = cache.store(data2)
print(key2)
print(cache.get(key2))

# Test case 4: Storing and retrieving binary data
data3 = b"third"
key3 = cache.store(data3)
print(key3)
print(cache.get(key3))

# Verify the call count of the store method
print(cache.get(cache.store.__qualname__))

# Additional test cases for type conversion
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

# Test case for call_history
s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
