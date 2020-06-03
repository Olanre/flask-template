import time 
import os, sys
import shutil
from app.drivers.db.store import Store
from app.drivers.db.metadata_service import MetadataService
from app.drivers.db.file_system.file_reader import FileReader
from app.drivers.db.file_system.file_writer import FileWriter
from app.drivers.db.lru_cache import LRUCache
from logger import log


class FileSystemBuilder:
    def __init__(self):
        self._instance = None

    #this method makes this class a singleton as only one instance is returned given the same arguments
    def __call__(self, partitions, service_root, expiration_time, **_ignored):
        if not self._instance:
            self._instance = FileSystemStore(partitions, service_root, expiration_time)
        return self._instance


class FileSystemStore(Store):

    def __init__(self, partitions = 10, service_root = os.getcwd(), expiration_time = 3600):
        self._partitions = ["partition_"+str(i) for i in range(partitions)]
        self._service_root = service_root
        self._expiration_time = expiration_time
        self._metadata_service = MetadataService(self._partitions)
        self.make_partitions_on_disk()
        #ideally use a LRU cache with a capacity of around 1k elements.
        self._small_cache = LRUCache(100)
        log.debug(f"Init of persistent filesystem based storage complete: expiration time is: {expiration_time}, service_root: {service_root} and node cluster partitions: {partitions}")

    def make_partitions_on_disk(self):
        for partition in self._partitions:
            path = self._service_root + partition
            try:
                os.mkdir(path)
                log.debug(f"Successfully created directory on path: {path}")
            except:
                log.error(f"The directory {path} could not be created")

           
    def put(self, id, data):
        partition = self._metadata_service.get_node(id)
        log.debug(f"Cluster location  where the  item {id} should be written to is {partition}")
        if not partition:
            return None
        filename = self._service_root + partition + id
        log.debug(f"Get is using the filename: {filename} to write the value for key: {id}")
        wr = FileWriter()
        wr.write_to_file(data, False, filename)
        self._small_cache.put(id, data)
        log.debug(f"Successfully wrote data item: {data} into the the persistent disk storage under filename: {filename}")
        
    def get(self, id):
        #use the small in memory cache if possible
        if id in self._small_cache:
            log.debug(f"Retrieved item {id} from the LUR cache")
            return self._small_cache.get(id)

        partition = self._metadata_service.get_node(id)
        log.debug(f"Cluster location  where the  item: {id} can be found is: {partition}")
        if not partition:
            return None
        filename = self._service_root + partition + id
        log.debug(f"Get is using the filename: {filename} to lookup the value for key: {id}")
        rd = FileReader()
        content =  rd.read_file(filename)
        log.debug(f"Retrieved item: {id} from the persistent disk storage from filename: {filename}")
        return content

    def remove(self, id):
        partition = self._metadata_service.get_node(id)
        filename = self._service_root + partition + id
        log.debug(f"Remove operation is using filename: {filename} for seeking")
        wr = FileWriter()
        wr.delete_file(filename)
        log.debug(f"Removed: {id} entry from the persistent disk storage")

    def clear(self):
        for partition in self._partitions:
            path = self._service_root + partition
            try:
                #Need a find a safe way to delete directories
                log.info(f"Cleared all elements from the persistent disk storage")
            except:
                log.error(f"The directory: {path} could not be deleted")

    def get_all(self):
        final_list = []
        for id, partition in self._metadata_service.get_all_metadata():
            data = self.get(id)
            final_list.append(id, data)
        log.info(f"Retrieved the following from the persistent disk storage: {final_list}")
        return final_list

                

