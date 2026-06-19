# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
p   1  [1,2,3]
   / \
  2   3 

q   1 [1,2,3]
   / \
  2   3
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.q_list = []
        self.p_list = []
        # returns list of tree
        def tree_to_list_q(node):
            if not node:
                self.q_list.append(None)
                return
            self.q_list.append(node.val)

            tree_to_list_q(node.left)
            tree_to_list_q(node.right)
        def tree_to_list_p(node):
            if not node:
                self.p_list.append(None)
                return
            self.p_list.append(node.val)
            
            tree_to_list_p(node.left)
            tree_to_list_p(node.right)

            

        tree_to_list_p(p)
        tree_to_list_q(q)
        return self.q_list == self.p_list

        