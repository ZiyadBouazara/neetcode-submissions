# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_arr = []
        q_arr = []

        self.toList(p, p_arr)
        self.toList(q, q_arr)

        return p_arr == q_arr

    def toList(self, root, arr: list) -> None:
        if not root:
            arr.append(None)
            return
        
        arr.append(root.val)

        self.toList(root.left, arr)
        self.toList(root.right, arr)

