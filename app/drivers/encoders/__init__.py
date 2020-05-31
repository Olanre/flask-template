import app.drivers.abstract_factory
from  app.drivers.encoders import Base62Encoder, HashLibEncoder

factory = abstract_factory.AbstractFactory()
factory.register_instance('hashlib_encoder', HashLibEncoder)
factory.register_instance('base62_encoder', Base62Encoder)
