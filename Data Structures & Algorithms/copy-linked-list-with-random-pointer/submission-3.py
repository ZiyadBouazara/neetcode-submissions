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
        #  head = [[3,null],[7,3],[4,0],[5,1]]
        # { Node1: Copy1, None2: Copy2, Node3: Copy3 }

        n_map = {}

        curr = head
        while curr:
            n_map[curr] = Node(x=curr.val)
            curr = curr.next
        
        curr2 = head
        while curr2:

            n_map[curr2].next = n_map[curr2.next] if curr2.next else None
            n_map[curr2].random = n_map[curr2.random] if curr2.random else None
            curr2 = curr2.next
        
        return n_map[head] if head else head
