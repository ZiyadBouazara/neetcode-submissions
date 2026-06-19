# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
        1
        /
       2
      /\
     3  5
    /    \
   4       6
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        self.res = 0
    
        def DFS(node):
            if not node:
                return 0

            length_left = DFS(node.left)
            length_right = DFS(node.right)
            self.res = max(self.res, length_left + length_right)

            return max(length_left, length_right) + 1

        DFS(root)
        return self.res

