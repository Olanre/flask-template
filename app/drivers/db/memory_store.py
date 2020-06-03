
import time
from app.drivers.db.store import Store
from logger import log


class MemoryStoreBuilder:
    def __init__(self):
        self._instance = None

    #this method makes this class a singleton as only one instance is returned given the same arguments
    #only use the argument we need, ignore all others
    def __call__(self, expiration_time, **_ignored):
        if not self._instance:
            self._instance = MemoryStore(expiration_time,)
        return self._instance

class MemoryStore(Store):

    def __init__(self, expiration_time = 3600):
        self._id_dict = {}
        self._time_to_live = {}
        self._expiration_time = expiration_time
        log.debug(f"Init of in-memory database complete. expiration time is: {expiration_time}")

    def put(self, id, data):
        if id not in self._id_dict:
            self._id_dict[id] = data
            self._time_to_live[id] = int(time.time()) + self._expiration_time
            log.debug(f"Inserted new value into the database with key: {id} and value: {data}")

    
    def get(self, id):
        try:
             item = self._id_dict[id]
             log.debug(f"Retrieved item {item} from the database using the key {id}")
             return item
        except:
            return None

    def get_all(self):
        if not self._id_dict:
            return None
        else:
            mylist = self._id_dict.items()
            log.debug(f"Retrieved the following from the database: {mylist}")
            return mylist
        
    def remove(self, id):
        del self._id_dict[id]
        log.info(f"Removed {id} entry from the database")
    
    def clear(self):
        self._id_dict = {}
        log.info("Cleared all elements from the database")