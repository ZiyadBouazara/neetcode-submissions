class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # O(n * 2**n)
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # O(n)
                return

            # decision 1: include current i
            subset.append(nums[i])
            dfs(i + 1)
            # decision 2: exclude current i
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res