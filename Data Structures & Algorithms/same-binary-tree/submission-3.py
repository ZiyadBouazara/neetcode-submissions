# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
p   1  [1,2,3]
   / \
  3   2 

q   1 [1,2,3]
     \
      3
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.is_same = True

        def compare_nodes(node1, node2):
            if not node1 and not node2: # both of them are None -> Were fine, continue !
                return
            
            if not node1 or not node2: # one of them is None, so we stop
                self.is_same = False
                return
            
            if node1.val != node2.val: # both are not None, we compare
                self.is_same = False
                return
            
            compare_nodes(node1.left, node2.left)
            compare_nodes(node1.right, node2.right)
        
        compare_nodes(p, q)
        return self.is_same


        