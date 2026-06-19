class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use a set
        # iteratively add elements to it and membership testing.
        hset = set()

        for d in nums:
            if d in hset:
                return d
            hset.add(d)

        