import abc

class abstractMetadataService(metaclass=abc.ABCMeta):
    """
    This is an abstract class for implementing a file metadata service
    which olds references on disk to a file based on a hash of its key and some 
    other metadata content to create a consistent hash algorithm
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_entry') and 
                callable(subclass.get_entry) and 
                hasattr(subclass, 'create_partition') and 
                callable(subclass.create_partition) and
                hasattr(subclass, 'get_all_metadata') and 
                callable(subclass.get_all_metadata))

    @abc.abstractmethod
    def get_entry(self, key):
        raise NotImplemented

    @abc.abstractmethod
    def create_partition(self, value):
        raise NotImplemented

    @abc.abstractmethod
    def get_all_metadata(self):
        raise NotImplemented