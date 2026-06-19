class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {} # key: node

        # dummy nodes : LRU and MRU
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1

        self._remove(self.hmap[key])
        self._insert(self.hmap[key])

        return self.hmap[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self._remove(self.hmap[key])

        self.hmap[key] = Node(key, value)
        self._insert(self.hmap[key])

        if len(self.hmap) > self.capacity:
            # remove lru
            lru = self.left.next
            self._remove(lru)
            del self.hmap[lru.key]

    # insert node at right
    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev  = node
        node.prev, node.next = prev, nxt
    
    # remove node from linked list
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


