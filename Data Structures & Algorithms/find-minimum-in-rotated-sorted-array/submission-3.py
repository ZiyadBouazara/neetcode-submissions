class Solution:
    def findMin(self, nums: List[int]) -> int:

        # nums = [8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7]
        minimum = float("inf")

        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (r + l) // 2
            minimum = min(minimum, nums[middle])

            # move pointers

            if nums[middle] < nums[-1]:
                # search left of middle
                r = middle - 1
            elif nums[middle] >= nums[-1]:
                # search right of middle
                l = middle + 1
        

        return minimum
        