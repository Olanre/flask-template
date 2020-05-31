from uhashring import HashRing
from app.drivers.db.abstract_metadata_service import abstractMetadataService

class MetadataService(abstractMetadataService):
    def __init__(self, nodes = ["node_1"]):
        self._nodes = nodes
        self._hr = HashRing(nodes=nodes)
        self._key_to_node = {}

    def get_node(self, key):
        hashed_key = self._hr.get_key(key)
        node = self._hr.get_node(hashed_key)
        self._key_to_node[key] = node
        return node

    def create_node(self, node_name):
        self._hr.add_node(node_name)
        self.nodes.append(node_name)

    def get_all_metadata(self):
        return self._key_to_node.items()

    def get_all_keys_for_node(self, node_name):
        return [key for key,node in self._nodes if node == node_name ]

    #TODO, allow reconstruction from a config file in case of power loss
    def reconstruct_from_config(self, config):
        pass

