import abc

class abstractFileReader(metaclass=abc.ABCMeta):
    """
    This is an abstract class for implmenting a file reader which can 
    read the content of a file, perform searching of a substring
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read_file') and 
                callable(subclass.read_file) and
                hasattr(subclass, 'is_substring_in_file') and 
                callable(subclass.is_substring_in_file))

    @abc.abstractmethod
    def read_file(self, filename):
        raise NotImplemented

    @abc.abstractmethod
    def is_substring_in_file(self, filename, substring):
        raise NotImplemented

    



