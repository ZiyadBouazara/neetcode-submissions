class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []
        while r < len(nums):
            curr_max = -float("inf")

            for num in nums[l:r + 1]:
                curr_max = max(curr_max, num)

            res.append(curr_max)

            l += 1
            r += 1
        return res
        