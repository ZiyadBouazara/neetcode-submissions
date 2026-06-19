class Solution:
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # if we see that the next element in the nums array is a duplicate, we have to block the right branch from duplicating the subset
        nums.sort()
        res = []

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            # decision 1: pick i in subset
            curr.append(nums[i])
            dfs(i+1, curr)
            # decision 2: skip i
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            curr.pop()
            dfs(i+1, curr)
        
        dfs(0, [])
        return res