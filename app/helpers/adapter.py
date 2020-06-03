class Adapter:
    """
    Adapts an object by replacing methods.
    From: https://www.youtube.com/watch?v=bsyjSW46TDg&t=708s 11:00
    Usage:
        test_obj = MyObject()
        test_obj_adapter = Adapter(test_obj, call_me = "special_call_me")
        test_obj_adapter.call_me -> this will call the actual objects 'special_call_me'
    """
    _initialized = False

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        for key, value in adapted_methods.items():
            func = getattr(self.obj, value)
            self.__setattr__(key, func)
        self._initialized = True

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def __setattr__(self, key, value):
        """  set attributes normally during initialization """
        if not self._initialized:
            super().__setattr__(key,value)
        else:
            """ Set attributed on minion after initialization"""
            setattr(self.obj, key, value)


    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__
