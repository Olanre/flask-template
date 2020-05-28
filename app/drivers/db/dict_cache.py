class dict_cache(Cache):

    def __init__(self):
        self._dict = {}

    def put(self, key, value):
        self._dict[key] = value
    
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