"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {} # oldNode: copyNode

        curr = head
        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            curr_res = hmap[curr]
            curr_res.next = hmap[curr.next] if curr.next else None
            curr_res.random = hmap[curr.random] if curr.random else None

            curr = curr.next

        return hmap[head] if head else None
        