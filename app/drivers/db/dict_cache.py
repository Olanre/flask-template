
import time
from app.drivers.db.cache import Cache

class DictCacheBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, expiration_time):
        if not self._instance:
            self._instance = DictCache(expiration_time)
        return self._instance

class DictCache(Cache):

    def __init__(self, expiration_time = 3600):
        self._dict = {}
        self._time_to_live = {}
        self._expiration_time = expiration_time

    def put(self, key, value):
        if key not in self._dict:
            self._dict[key] = value
            self._time_to_live[key] = int(time.time()) + self._expiration_time

    
    def get(self, key):
        try:
             self._dict[key]
        except:
            return None

    def get_all(self):
        if not self._dict:
            return None
        else:
            return self._dict.items()
        
    def remove(self, key):
        del self._dict[key]
    
    def clear(self):
        self._dict = {}