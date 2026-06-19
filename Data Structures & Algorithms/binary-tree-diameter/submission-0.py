# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = right side depth + left side depth
        height = self.findHeight(root) - 1

        return max(height, self.diameter)

    def findHeight(self, root):
        if not root:
            return 0
        
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)

        if left + right > self.diameter:
            self.diameter = left + right
        
        return 1 + max(left, right)
