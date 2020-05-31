import abc

class abstractFileWriter(metaclass=abc.ABCMeta):
    """
    This is an abstract class for implmenting a file writer
    which can create files, write to files and delete files
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'create_file') and 
                callable(subclass.create_file) and 
                hasattr(subclass, 'write_to_file') and 
                callable(subclass.write_to_file) and
                hasattr(subclass, 'delete_file') and 
                callable(subclass.delete_file))

    @abc.abstractmethod
    def create_file(self, overwrite_if_exists):
        raise NotImplemented

    @abc.abstractmethod
    def delete_file(self):
        raise NotImplemented

    @abc.abstractmethod
    def write_to_file(self, content, append,  delimiter):
        raise NotImplemented


    



