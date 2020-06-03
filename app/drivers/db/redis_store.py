from redis import Redis
from app.drivers.db.store import Store
from logger import log

class RedisStoreBuilder:
    def __init__(self):
        self._instance = None

    #this method makes this class a singleton as only one instance is returned given the same arguments
    def __call__(self, host = "localhost", port=6379, db=0,  prefix = "", expiration_time=3600, **_ignored):
        if not self._instance:
            self._instance = RedisStore(host, port, db, prefix, expiration_time)
        return self._instance


class RedisStore(Store):
    """
    This cach allows us to abstract the driver for Redis
    r = RedisStore
    r.put("a", 1)
    r.get("a") # returns '1'
    r.put("b","two")
    r.get("b") #returns 2

    This requires redis to work
    """

    def __init__(self, host = "127.0.0.1", port=6379, db=0,  prefix = "", expiration_time=3600):
        """
        Initialize a database defined by the connection provided

        Input:
            host: the host to connect to the redis server, default is localhost
            port: The port number to connect on, default is 6379
            db: the redis database, default is 0
        """
        self._redis = Redis(host, port, db)
        self.prefix = prefix
        self.expiration_time = expiration_time
        log.debug("Init of redis database complete. host: {host}, port: {port}, db instance: {db}, expiration time for elements: {expiration_time}")

    def put(self, key, value):
        """
        inserts a new  object into the cache defined by the key and value
        input:
        key: The key for the cache object to be insert
        value: The value pointed to by the key
        expiration_time: The time to wait until the object is removed from the cache which defaults to 3600 seconds.
        Raises: 
        redis.exceptions.ConnectionError: An error if there is some problem on the connection
        with Redis server.
        """
        self.redis.setex(self.prefix + key, value, self.expiration_time)
        log.debug("Inserted new value into the database with key: {key} and value: {value}")

    def get(self, key):
        """
        gets the object from the cache indexed by the key
        input:
            key: The key for the cache object to retrieved
        Raises: 
            redis.exceptions.ConnectionError: An error if there is some problem on the connection
                with Redis server.
        """

        item =  self.redis.get(self.prefix + key)
        log.debug("Retrieved item {item} from the database using the key {key}")
        return item

    def remove(self, key):
        """
        Remove the object indexed by the key from the cache 
        input
            key: The key for the cache object to be removed

        Raises:
            redis.exceptions.ConnectionError: An error if there is some problem on the connection
                with Redis server.

        """
        
        self.redis.lpop(self.prefix + key)
        log.debug("Removed {key} entry from the database")

    def get_all(self):
        """
        Gets all the objects in the cache 
        input
            key: The key for the cache object to be removed

        Raises:
            redis.exceptions.ConnectionError: An error if there is some problem on the connection
                with Redis server.

        """
        mylist = []
        for key in self.redis.scan_iter(self.prefix+":*"): 
            value = self.redis.get(self.prefix + key)
            mylist.append((key,value))
        log.info("Retrieved the following from the database: {mylist}")
        return mylist
    
    def clear(self):
        """
        Deletes all the objects in the cache

        Raises:
            redis.exceptions.ConnectionError: An error if there is some problem on the connection
                with Redis server.

        """
        self.redis.flushdb()
        log.info("Cleared all elements from the database")