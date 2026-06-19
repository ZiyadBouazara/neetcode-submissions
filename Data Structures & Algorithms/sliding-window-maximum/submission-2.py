class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []
        while r < len(nums):
            curr_max = max(nums[l: r+1])
            res.append(curr_max)

            l += 1
            r += 1
        return res
        