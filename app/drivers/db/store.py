import abc

class Store(metaclass=abc.ABCMeta):
    """
    This is an abstract class for implmenting a key value store
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
    def put(self, id, data):
        raise NotImplemented


    @abc.abstractmethod
    def get(self, id):
        raise NotImplemented

    @abc.abstractmethod
    def remove(self, id):
        raise NotImplemented

    @abc.abstractmethod
    def clear(self):
        raise NotImplemented


    @abc.abstractmethod
    def get_all(self):
        raise NotImplemented

    



