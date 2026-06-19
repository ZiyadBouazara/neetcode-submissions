class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashmap = {}

        # for i in range(len(numbers)):
        #     diff = target - numbers[i]

        #     if (diff) in hashmap:
        #         return [hashmap[diff], i+1]

        #     hashmap[numbers[i]] = i+1

        left = 0
        right = len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]

            if summ == target:
                return [left+1, right+1]
            elif summ > target:
                right -= 1
            elif summ < target:
                left += 1




        