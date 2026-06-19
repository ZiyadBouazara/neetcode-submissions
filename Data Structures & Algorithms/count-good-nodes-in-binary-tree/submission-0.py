# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs on all paths -> store nodes of path -> if max(nodes) == curr_node -> count+1
        curr_max = float("-inf")
        self.res = 0

        self.dfs(root, curr_max)

        return self.res

    def dfs(self, node, curr_max) -> None:
        if not node:
            return
        
        if node.val >= curr_max:
            self.res += 1
            curr_max = node.val

        self.dfs(node.left, curr_max)
        self.dfs(node.right, curr_max)