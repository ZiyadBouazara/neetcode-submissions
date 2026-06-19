class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        total = 0

        while l<r:
            if maxL < maxR:
                l += 1
                total += max(maxL - height[l], 0)
                maxL = max(maxL, height[l])
            else:
                r -= 1
                total += max(maxR - height[r], 0)
                maxR = max(maxR, height[r])
        return total