#!/usr/bin/env python3

''' Module defining child class FIFOCache
'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''Inherits from BaseCaching
    '''
    def __init__(self):
        ''' Overloads the child class
        '''
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        ''' Put a value item to the Cache_data dict
        based on the key
        '''
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return key

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        ''' Get value from the Cache_data dict
        base on the the key
        '''
        if key in self.cache_data:
            return self.cache_data[key]
        return None
