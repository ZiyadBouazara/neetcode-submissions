# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))
    
    def valid(self, node, left, right):
        if not node:
            return True
        
        if not (left < node.val < right):
            return False
        
        left_bool = self.valid(node.left, left, node.val)
        right_bool = self.valid(node.right, node.val, right)

        return left_bool and right_bool