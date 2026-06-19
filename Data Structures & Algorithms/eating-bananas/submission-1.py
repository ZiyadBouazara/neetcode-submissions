class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            middle_k = (l+r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / middle_k)

            if hours <= h:
                res = middle_k
                r = middle_k - 1
            else:
                l = middle_k + 1
        return res