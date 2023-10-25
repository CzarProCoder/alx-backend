#!/usr/bin/env python3

'''
Module defining child class BasicCache
'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    Subclass inheriting from BaseCaching
    Must use the cache_data from the parent class
    '''
    def put(self, key, item):
        '''
        Attach a value (item) to the dictionaty
        based on the key
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Get the dictionary value based on the key
        '''
        if key:
            return (self.cache_data.get(key))
        return None
