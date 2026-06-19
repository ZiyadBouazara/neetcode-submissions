class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # take smallest h between the two and calcuate area (j-i * smallest h)

        area = 0
        n = len(heights)
        l ,r = 0, n - 1

        while l < r:
            smallest_h = heights[l] if heights[l] < heights[r] else heights[r]
            curr_area = (r - l) * smallest_h

            if curr_area > area:
                area = curr_area

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return area

# area = 2


# smallest_h = 1
# curr_area = 2
# i = 0
# j = 2