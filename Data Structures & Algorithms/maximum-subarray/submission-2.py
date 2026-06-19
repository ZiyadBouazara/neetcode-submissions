class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = float("-inf")

        for i in range(len(nums)):
            curr_sum = nums[i]
            res = max(res, curr_sum)
            for j in range(i+1, len(nums)):
                curr_sum += nums[j]
                res = max(res, curr_sum)
                print(res)

        return res
