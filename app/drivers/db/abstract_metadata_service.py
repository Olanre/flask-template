import abc

class abstractMetadataService(metaclass=abc.ABCMeta):
    """
    This is an abstract class for implementing a file metadata service
    which olds references on disk to a file based on a hash of its key and some 
    other metadata content to create a consistent hash algorithm
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_node') and 
                callable(subclass.get_node) and 
                hasattr(subclass, 'create_node') and 
                callable(subclass.create_node) and
                hasattr(subclass, 'get_all_metadata') and 
                callable(subclass.get_all_metadata))

    @abc.abstractmethod
    def get_node(self, key):
        raise NotImplemented

    @abc.abstractmethod
    def create_node(self, value):
        raise NotImplemented

    @abc.abstractmethod
    def get_all_metadata(self):
        raise NotImplemented