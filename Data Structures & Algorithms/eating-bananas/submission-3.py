class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force -> 
        # sort list
        #                  1 <= k <= max(piles)

        maximum = max(piles) # O(n)
        k = float("inf")
        l, r = 1, maximum

        while l <= r: # O(n * logm)
            middle = (r+l) // 2
            curr_h = 0
            for num in piles:
                curr_h += math.ceil(num / middle) # number of hours it takes with middle eating speed
            
            if curr_h <= h:
                k = min(k, middle)
                r = middle - 1
            else:
                l = middle + 1
        
        return k


        # O(m * n)
        # i = 2
        # curr_h = 6
        # [1, 2, 3, 4]

