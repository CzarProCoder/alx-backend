#!/usr/bin/env python3

''' Module defining child class FIFOCache
'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
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
