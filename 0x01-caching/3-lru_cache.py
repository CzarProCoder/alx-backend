#!/usr/bin/env python3

''' Module defining child class LRUCache
'''

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''Inherits from BaseCaching
    '''
    def __init__(self):
        ''' Overloads the child class
        '''
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        ''' Put a value item to the Cache_data dict
        based on the key
        '''
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.lru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.lru_order) > BaseCaching.MAX_ITEMS:
            self.lru_order.popitem(last=False)

    def get(self, key):
        ''' Get value from the Cache_data dict
        base on the the key
        '''
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
