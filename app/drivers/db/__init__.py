from logger import log

from  app.drivers.db.memory_store import MemoryStoreBuilder
from  app.drivers.db.redis_store import RedisStoreBuilder
from app.drivers.db.file_system.file_system_store import FileSystemBuilder
from app.factories.abstract_factory import AbstractFactory

log.debug("Registering datastore implementations through the factory builder")
factory = AbstractFactory()
factory.register_instance('memory', MemoryStoreBuilder())
factory.register_instance('redis', RedisStoreBuilder())
factory.register_instance('filesystem', FileSystemBuilder())

