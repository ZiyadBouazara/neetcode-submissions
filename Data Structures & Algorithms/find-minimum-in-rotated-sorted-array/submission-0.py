class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = float("inf")
        while l <= r:
            middle = (l+r) // 2

            if nums[middle] < nums[r]:
                res = min(nums[middle], res)
                r = middle - 1
            else:
                res = min(nums[middle], res)
                l = middle + 1
        return res