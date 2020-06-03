import abc
class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'update') and 
                callable(subclass.update) )

    @abc.abstractmethod
    def update(self):
        raise NotImplemented
