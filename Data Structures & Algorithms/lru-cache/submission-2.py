class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val  = val 
        self.prev = None 
        self.next = None 


class LRUCache:
    """
    LRU Cache: 

    Doubly linked list with most recently used on the left

    """

    def __init__(self, capacity: int):
        """Initalizes the LRU Cache, must hae positive size capacity"""
        self.capacity = capacity
        self.mapping = {}

        self.dummy_left = ListNode(None, None)
        self.dummy_right = ListNode(None, None)
        self.dummy_left.next = self.dummy_right
        self.dummy_right.prev = self.dummy_left
        self.curr_count = 0

    def insertNodeLeft(self, start, new_node):
        prev_node = start.prev 
        prev_node.next = new_node 
        new_node.prev = prev_node 

        new_node.next = start 
        start.prev = new_node
        

    def removeNode(self, node):
        prevNode = node.prev 
        nextNode = node.next 
        prevNode.next = nextNode 
        nextNode.prev = prevNode

        

    def get(self, key: int) -> int:
        """
        Returns the value of the key if exists otherwise -1
        """
        if key in self.mapping:
            result = self.mapping[key]
            # now insert it to the left 
            self.removeNode(result)
            self.insertNodeLeft(self.dummy_left.next, result)
            return result.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if exists. POtherwise add the key,value pair to cache. If exceed capacity, evect the leasdt recently used key"""
        if key in self.mapping:
            node = self.mapping[key]
            node.val = value
            self.removeNode(node)
            self.insertNodeLeft(self.dummy_left.next,node)

    
        else:
            new_node = ListNode(key, value)
            self.curr_count += 1

            if self.curr_count > self.capacity:
                temp = self.dummy_right.prev
                self.removeNode(temp)
                self.insertNodeLeft(self.dummy_left.next, new_node)
                self.curr_count -= 1
                self.mapping.pop(temp.key)
            else:
                self.insertNodeLeft(self.dummy_left.next, new_node)

            self.mapping[key] = new_node 

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)