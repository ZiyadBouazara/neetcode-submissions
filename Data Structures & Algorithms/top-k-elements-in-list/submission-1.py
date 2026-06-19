class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, value in count.items():
            freq[value].append(key)
        
        result = []
        for array in reversed(freq):
            for num in array:
                result.append(num)
                if len(result) == k:
                    return result
            
