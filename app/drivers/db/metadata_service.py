from uhashring import HashRing
from app.drivers.db.abstract_metadata_service import abstractMetadataService
from logger import log

class MetadataService(abstractMetadataService):
    def __init__(self, nodes = ["node_1"]):
        self._nodes = nodes
        self._hr = HashRing(nodes=nodes)
        self._key_to_node = {}
        log.debug(f"Init of Metadata Service is complete. Nodes are: {nodes}")

    def get_node(self, key):
        hashed_key = self._hr.get_key(key)
        log.debug(f"Retrieved hashed key: {hashed_key} from key: {key} from the hashring")
        node = self._hr.get_node(hashed_key)
        log.debug(f"The node to associated with the hashed key: {hashed_key} is: {node}")
        self._key_to_node[key] = node
        return node

    def create_node(self, node_name):
        self._hr.add_node(node_name)
        self.nodes.append(node_name)
        log.debug(f"Added the node: {node_name} to the hashring")

    def get_all_metadata(self):
        all_items =  self._key_to_node.items()
        log.debug(f"All the items in the metadata service are: {all_items}")
        return all_items

    def get_all_keys_for_node(self, node_name):
        key_list =  [key for key,node in self._nodes if node == node_name ]
        log.debug(f"The mapping of keys to nodes in the metadata service is: {key_list}")

    #TODO, allow reconstruction from a config file in case of power loss
    def reconstruct_from_config(self, config):
        pass

