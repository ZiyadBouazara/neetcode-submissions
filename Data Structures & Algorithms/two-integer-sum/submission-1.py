class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                if hashmap[diff] != i:
                    return [i, hashmap[diff]]