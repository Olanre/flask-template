import abc

class AbstractPublisher(metaclass=abc.ABCMeta):
    """
    This is an abstract class for implmenting an abstract observer
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'add') and 
                callable(subclass.add) and 
                hasattr(subclass, 'remove') and 
                callable(subclass.remove) and
                hasattr(subclass, 'notify') and
                callable(subclass.notify))

    @abc.abstractmethod
    def add(self, object):
        raise NotImplemented

    @abc.abstractmethod
    def remove(self, object):
        raise NotImplemented

    @abc.abstractmethod
    def notify(self):
        raise NotImplemented