class Node:
        def __init__(self, key, val):
            # Curr points
            self.next = self.prev = None 
            #key
            self.key = key
            # value
            self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # initaitve dummy values
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.end_ptr = self.right
        

    def delete(self, node:Node):
        left_ptr = node.prev
        right_ptr = node.next 

        left_ptr.next = right_ptr
        right_ptr.prev = left_ptr
    
    def add(self, node:Node):
        # add specific node to the front of the linked list
        prev_ptr = self.end_ptr.prev
        future_ptr = prev_ptr.next

        prev_ptr.next = node
        node.prev = prev_ptr 
        node.next = future_ptr
        future_ptr.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            result = self.cache[key].val
            # remove first then update
            self.delete(self.cache[key])
            #update to correct position
            self.add(self.cache[key]) #adds to the front of the linked list
            return result



    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value

            self.delete(self.cache[key])
            self.add(self.cache[key])
        
        else:
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
        
        # exceeded the limit
        if len(self.cache) > self.capacity:
            temp = self.left.next.key
            self.delete(self.cache[self.left.next.key])
            # Get rid of the next 
            self.cache.pop(temp)
        
        
