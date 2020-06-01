import time 
import os, sys
import shutil
from app.drivers.db.cache import Cache
from app.drivers.db.metadata_service import MetadataService
from app.drivers.db.file_system.file_reader import FileReader
from app.drivers.db.file_system.file_writer import FileWriter
from app.drivers.db.lru_cache import LRUCache


class FileSystemBuilder:
    def __init__(self):
        self._instance = None

    #this method makes this class a singleton as only one instance is returned given the same arguments
    def __call__(self, partitions, service_root, expiration_time, **_ignored):
        if not self._instance:
            self._instance = FileSystemStore(partitions, service_root, expiration_time)
        return self._instance


class FileSystemStore(Cache):

    def __init__(self, partitions = 10, service_root = os.getcwd(), expiration_time = 3600):
        self._partitions = ["partition_"+str(i) for i in range(partitions)]
        self._service_root = service_root
        self._expiration_time = expiration_time
        self._metadata_service = MetadataService(self._partitions)
        #ideally use a LRU cache with a capacity of around 1k elements.
        self._small_cache = LRUCache(100)

    def make_partitions_on_disk(self):
        for partition in self._partitions:
            path = self._service_root + partition
            try:
                os.mkdir(path)
            except:
                print("The directory {} could not be created".format(path))

           
    def put(self, key, value):
        partition = self._metadata_service.get_node(key)
        if not partition:
            return None
        filename = self._service_root + partition + key
        wr = FileWriter(filename)
        wr.write_to_file(value, False)
        self._small_cache.put(key, value)
        
    def get(self, key):
        #use the small in memory cache if possible
        if key in self._small_cache:
            return self._small_cache.get(key)

        partition = self._metadata_service.get_node(key)
        if not partition:
            return None
        filename = self._service_root + partition + key
        rd = FileReader(filename)
        content, c_date =  rd.read_file()
        return content

    def remove(self, key):
        partition = self._metadata_service.get_node(key)
        filename = self._service_root + partition + key
        wr = FileWriter(filename)
        return wr.delete_file()

    def clear(self):
        for partition in self._partitions:
            path = self._service_root + partition
            try:
                #Need a find a safe way to delete directories
                print("Purging Cache")
            except:
                print("The directory {} could not be deleted".format(path))

    def get_all(self):
        final_list = []
        for key, partition in self._metadata_service.get_all_metadata():
            value = self.get(key)
            final_list.append(key, value)
        return final_list

                

