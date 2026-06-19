class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ROWS, COLS = len(matrix), len(matrix[0])

        # top, bot = 0, ROWS - 1
        # while top <= bot:
        #     row = (top + bot) // 2
        #     if target > matrix[row][-1]:
        #         top = row + 1
        #     elif target < matrix[row][0]:
        #         bot = row - 1
        #     else:
        #         break

        # if top > bot:
        #     return False
        # row = (top + bot) // 2
        # l, r = 0, COLS - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if target > matrix[row][m]:
        #         l = m + 1
        #     elif target < matrix[row][m]:
        #         r = m - 1
        #     else:
        #         return True
        # return False
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1 # 0,0

        while top <= bot:
            mid = (top+bot) // 2 # 0

            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        if top > bot:
            return False
        
        l, r = 0, COLS - 1

        search_row = matrix[((top+bot) // 2)]

        while l <= r:
            mid = (l+r) // 2
            if target < search_row[mid]:
                r = mid - 1
            elif target > search_row[mid]:
                l = mid + 1
            else:
                return True

        return False


































