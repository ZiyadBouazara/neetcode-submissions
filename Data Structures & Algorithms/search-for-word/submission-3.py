class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        board=[
            ["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"]]


        word="ABCESEEEFS"
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(seen, i, r, c):
            if i == len(word):
                return True
            
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
            (r, c) in seen or board[r][c] != word[i]): # if out of bounds
                return False
            
            seen.add((r, c))
            res = dfs(seen, i+1, r+1, c) or dfs(seen, i+1, r-1, c) or dfs(seen, i+1, r, c+1) or dfs(seen, i+1, r, c-1)
            seen.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(set(), 0, r, c):
                    return True

        return False