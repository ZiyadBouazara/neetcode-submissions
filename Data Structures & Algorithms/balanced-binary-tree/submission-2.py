# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
        1(d=2)
       / \
      2   3(d=2)
         / \
        4   6
       /
      5  

is_balanced = True
===node 1===
height_l = 1
height_r = 3
===node 3===
height_l = 2
height_r = 1 
        """
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        
        # returns height of a node
        def dfs(node):
            if not node:
                return 0
            
            height_l = dfs(node.left)
            height_r = dfs(node.right)
            if abs(height_l - height_r) > 1:
                self.is_balanced = False

            return max(height_l, height_r) + 1
        
        dfs(root)
        return self.is_balanced
    