class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, seen):
            if len(curr) >= len(nums):
                res.append(curr.copy())
            
            for i in range(len(nums)):
                if not seen[i]:
                    curr.append(nums[i])
                    seen[i] = True
                    dfs(curr, seen)
                    seen[i] = False
                    curr.pop()

        

        dfs([], [False] * len(nums))
        return res