class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # create dummy
        self.head = Node(-1,-1)
        self.tail = Node(-1, -1)

        # connect the dummy nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        # point to the back and front node
        front = node.next
        back = node.prev
        # connect the prev and front 
        back.next = front
        front.prev = back
        # removed node point to node
        node.next = None
        node.prev = None

    def insert(self, node):

        # keep the front node
        front = self.head.next

        # point the head and front node to new added node
        self.head.next = node
        front.prev = node

        # move nodes pointer to the back and front
        node.prev = self.head
        node.next = front
        
    def get(self, key: int) -> int:
        # if exist
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val

        # does not exist
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        # if exist
        if key in self.cache:
            # change the value of the node
            prev_node = self.cache[key]
            prev_node.val = value

            # move it to front
            self.remove(prev_node)
            self.insert(prev_node)
        else:
            new_node = Node(key, value)
            # has capacity to add
            if self.cap > len(self.cache):
                # insert the value in to the linked list and cache
                self.insert(new_node)
                self.cache[key] = new_node
            # has no capacity
            else:
                # remove the last element from linked list
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
                # insert it in front
                self.insert(new_node)
                self.cache[key] = new_node
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)