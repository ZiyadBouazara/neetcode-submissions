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
        # tree has at least 2 nodes
        # p and q are both in root
        # p and q can be None

        self.LCA = root

        # p is on the left, q is on the right -> then LCA is current Node -> we can stop !
        def dfs(curr, p, q):
            self.LCA = curr
            if curr.val == p.val or curr.val == q.val:
                return
   
            splitting = (p.val < curr.val and q.val > curr.val) or (p.val > curr.val and q.val < curr.val)
            if splitting: 
                return
            
            if p.val < curr.val and q.val < curr.val:
                dfs(curr.left, p, q)
                return
            dfs(curr.right, p, q)
            return
        
        dfs(root, p, q)
        return self.LCA
            
        # both on the left or right -> update LCA
        # if p or q == current node -> return p or q
