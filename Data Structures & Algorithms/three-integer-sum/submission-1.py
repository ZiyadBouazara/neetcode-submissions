class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-4, -1, -1, 0, 1, 2]
        # hashset = [[-1,-1,2], [-1, 0, 1]]
        nums.sort()
        hashset = set() # triplets tuples
        n = len(nums)

        for i in range(n):
            # do some check for duplicate with i - 1 if i > 0
            l, r = i + 1, n - 1
            while l < r :
                summ = nums[i] + nums[l] + nums[r]

                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    if tuple([nums[i], nums[l], nums[r]]) not in hashset:
                        hashset.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
        output = []
        for t in hashset:
            output.append(list(t))
        return output