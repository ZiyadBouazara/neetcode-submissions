class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, seen):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for n in range(len(nums)):
                if not seen[n]:
                    curr.append(nums[n])
                    seen[n] = True
                    dfs(curr, seen)
                    curr.pop()
                    seen[n] = False

        
        dfs([], [False] * len(nums))
        return res