#!/usr/bin/env python3

'''Task 1: FIFO caching
'''


from collections import OrderedDict
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the first key inserted into the cache
            first_key = next(iter(self.cache_data))
            # Remove the first item from the cache
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}\n")

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
