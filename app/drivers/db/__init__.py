from  app.drivers.db.dict_cache import DictCacheBuilder
from  app.drivers.db.redis_cache import RedisCacheBuilder
from app.drivers.db.file_system.file_system_store import FileSystemBuilder
from app.factories.abstract_factory import AbstractFactory

factory = AbstractFactory()
factory.register_instance('memory', DictCacheBuilder())
factory.register_instance('redis', RedisCacheBuilder())
factory.register_instance('filesystem', FileSystemBuilder())

