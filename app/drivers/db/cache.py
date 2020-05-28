import abc

class cache(metaclass=abc.ABCMeta):
    """
    This is an abstract class for implmenting a key value cache
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'put') and 
                callable(subclass.put) and 
                hasattr(subclass, 'get') and 
                callable(subclass.get) and
                hasattr(subclass, 'remove') and 
                callable(subclass.remove) and
                hasattr(subclass, 'clear') and 
                callable(subclass.clear) and 
                hasattr(subclass, 'get_all') and 
                callable(subclass.get_all))

    @abc.abstractmethod
    def put(self, key, value):
        raise NotImplemented


    @abc.abstractmethod
    def get(self, key):
        raise NotImplemented

    @abc.abstractmethod
    def remove(self, key):
        raise NotImplemented

    @abc.abstractmethod
    def clear(self):
        raise NotImplemented


    @abc.abstractmethod
    def get_all(self):
        raise NotImplemented

    



