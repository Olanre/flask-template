class AbstractFactory:
    def __init__(self):
        self._instances = {}

    def register_instance(self, key, instance):
        self._instances[key] = instance

    def create(self, key, **kwargs):
        instance = self._instances.get(key)
        if not instance:
            raise ValueError(key)
        return instance(**kwargs)