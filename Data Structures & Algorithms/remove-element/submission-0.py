class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        for i in range(len(nums)):
            while i <= last and nums[last] == val:
                last -= 1
            if i >= last:
                break
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
        
        c = len(nums) -1

        while c >=0 and nums[c] == val:
            nums.pop()
            c -= 1
        return len(nums)