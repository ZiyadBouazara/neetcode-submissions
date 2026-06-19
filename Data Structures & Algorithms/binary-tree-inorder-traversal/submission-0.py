# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        1
      /    \
      2     3
     / \    /
        4  5    

    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        def in_order_traversal(node):
            if not node:
                return
            
            in_order_traversal(node.left)
            self.res.append(node.val)
            in_order_traversal(node.right)
        
        in_order_traversal(root)
        return self.res