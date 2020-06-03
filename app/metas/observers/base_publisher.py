class ObserverError(Exception):
    pass

class BasePublisher(AbstractPublisher):
    def __init__(self):
        self.observers = []
    
    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            raise ObserverError("Unable to add {} to the publisher".format(observer))
    
    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            raise ObserverError("Unable to remove {} from the publisher".format(observer))
    
    def notify(self):
        for observer in observers:
            observer.update(self)
