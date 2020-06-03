import abc

class BaseEncoder(metaclass=abc.ABCMeta):
    """
    This is an abstract class for implmenting a simple encoder/decoder serializer
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'encode') and 
                callable(subclass.put) and 
                hasattr(subclass, 'decode') and 
                callable(subclass.get))

    @abc.abstractmethod
    def encode(self, string):
        raise NotImplemented

    @abc.abstractmethod
    def decode(self, string):
        raise NotImplemented
