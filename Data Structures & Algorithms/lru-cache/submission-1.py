class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.capacity = capacity
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insert(self, node):
        nxt = self.start.next
        node.prev = self.start
        node.next = nxt
        nxt.prev = node
        self.start.next = node


    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            self.remove(node)
        
        node = Node(key, value)
        self.insert(node)
        self.hmap[key] = node

        if len(self.hmap) > self.capacity:
            lru = self.end.prev
            self.remove(lru)
            del self.hmap[lru.key]