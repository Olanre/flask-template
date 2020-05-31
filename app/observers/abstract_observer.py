import abc

class AbstractObserver(metaclass=abc.ABCMeta):
    """
    This is an abstract class for implmenting a key value cache
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'add') and 
                callable(subclass.put) and 
                hasattr(subclass, 'remove') and 
                callable(subclass.get) and
                hasattr(subclass, 'notify'))

    @abc.abstractmethod
    def add(self, object):
        raise NotImplemented

    @abc.abstractmethod
    def remove(self, object):
        raise NotImplemented

    @abc.abstractmethod
    def notify(self):
        raise NotImplemented