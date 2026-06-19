class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            middle = l + (r-l // 2)

            if target < nums[middle]:
                r = middle - 1
            elif target > nums[middle]:
                l = middle + 1
            else:
                return middle
        return -1

