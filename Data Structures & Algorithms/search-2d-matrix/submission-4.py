class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # two row pointers (t, b) -> take first element of middle row and compare with target
            # -> if target > middle element -> last element of row > target -> then target is in this row -> do a binary search in this row
                                            # -> last element of row < target -> move top pointer past this row
        t, b = 0, len(matrix) - 1

        while t <= b:
            m_row = (t + b) // 2

            if target > matrix[m_row][0]:
                if target <= matrix[m_row][-1]:
                    return self.binary_search(matrix[m_row], target)
                else:
                    t = m_row + 1
            elif target < matrix[m_row][0]:
                b = m_row - 1
            else:
                return True
        return False
    
    def binary_search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return True
        return False
