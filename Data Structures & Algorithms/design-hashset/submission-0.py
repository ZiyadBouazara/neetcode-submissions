class Node:
    
    def __init__(self, key=None, nxt=None) -> None:
        self.key = key
        self.nxt = nxt


class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.bucket = [Node()] * self.size
       
    def add(self, key: int) -> None:
        head = self.bucket[key % self.size]
        curr, prev = head, head
        while curr:
            if curr.key == key:
                return

            prev = curr
            curr = curr.nxt
            
        prev.nxt = Node(key)
         
    def remove(self, key: int) -> None:
        head = self.bucket[key % self.size]
        curr, prev = head, head
        while curr:
            if curr.key == key:
                prev.nxt = curr.nxt
                return

            prev = curr
            curr = curr.nxt
        
        
    def contains(self, key: int) -> bool:
        if self._search(key) is not None:
            return True
        return False     
        
    def _search(self, key: int) -> Node | None:
        head = self.bucket[key % self.size]
        curr, prev = head, head
        while curr:
            if curr.key == key:
                return curr

            prev = curr
            curr = curr.nxt
        return curr


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)