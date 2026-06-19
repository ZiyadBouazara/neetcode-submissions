class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for i in nums:
            count_map[i] = 1 + count_map.get(i, 0)
            if count_map[i] > 1:
                return True
        
        return False
