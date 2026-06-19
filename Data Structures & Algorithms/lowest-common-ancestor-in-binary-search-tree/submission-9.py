# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
p=9, q=7

        5
       /  \
      3    8
     / \  / \
    1  4  7  9
     \
      2
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val <= curr.val and q.val >= curr.val or p.val >= curr.val and q.val <= curr.val:
                break
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        return curr
            
