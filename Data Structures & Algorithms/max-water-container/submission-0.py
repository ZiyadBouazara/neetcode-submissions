class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                maximum = max(min(heights[i], heights[j]) * abs(i - j), maximum) # 0 - 2 = 2
        return maximum
