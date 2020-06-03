from collections import OrderedDict
from logger import log
from app.drivers.db.store import Store

class LRUCache(Store):

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
        log.debug("Init of LRU memory cache complete: set capacity: {capacity}")

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1
        val = self.cache[key]
        log.debug("Retrieved item {val} from the database using the key {key}")
        self.cache.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        log.debug("Inserted new value into the database with key: {key} and value: {value}")
        if len(self.cache) > self.size:
            log.info("Cache is at capacity, removing least recently used element")
            item = self.cache.popitem(last=False)
            log.info("Removed {item}, the least recent used element from the cache")

    def get_all(self):
        if not self.cache:
            return None
        else:
            mylist = self.cache.items()
            log.debug("Retrieved the following from the database: {mylist}")
            return mylist
        
    def remove(self, key):
        del self.cache[id]
        log.debug("Removed {key} entry from the database")
    
    def clear(self):
        self.cache = {}
        log.debug("Cleared all elements from the database")