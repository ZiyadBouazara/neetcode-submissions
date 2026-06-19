class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        dq = collections.deque() # index
        res = []

        l = 0
        for r in range(0, len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()

            dq.append(r)

            # shrink window
            if r - l + 1 > k:
                l += 1
                if dq[0] < l:
                    dq.popleft()

            if r - l + 1 == k:
                res.append(nums[dq[0]])
        
        return res


# res = [2, 2, 4, 4, 6]
# dq = [6]
# l, r = 3, 6
            




        