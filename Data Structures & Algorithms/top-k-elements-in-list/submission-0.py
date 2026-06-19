class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # construct dict with count using ->  number: count
        # construct array of sorted desc dict values ** not sure
        # return the sliced array using k -> [:k]
        counter_map = {}

        for num in nums:
            counter_map[num] = 1 + counter_map.get(num, 0)
        
        sorted_list = [key for key,value in sorted(counter_map.items(), key=lambda item: item[1], reverse=True)]
        return sorted_list[:k]

