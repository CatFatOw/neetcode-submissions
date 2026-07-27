
        

class LRUCache:

    class ListNode:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
        
        

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = self.ListNode(0,0)
        self.right = self.ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def add_end(self, node):

            self.right.prev.next = node
            node.prev = self.right.prev 

            node.next = self.right
            self.right.prev = node

            
    def remove_front(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_front(node)
            self.add_end(node)
            return node.val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # if the key is already in the cache we can update it 
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove_front(node)
            self.add_end(node)

        else:
            # if the capacity is overthrown 
            if len(self.cache) > self.capacity:
                node = self.cache[key]
                self.remove_front(node)
                self.cache.pop(key)
                self.add_front(self.ListNode(value))

                
               
            else:
                node = self.ListNode(key, value)
                self.cache[key] = node
                self.add_end(node)

                if len(self.cache) > self.capacity:
                    lru = self.left.next
                    self.remove_front(lru)
                    self.cache.pop(lru.key)

        
