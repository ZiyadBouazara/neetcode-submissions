class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(count_open, count_closed, curr):
            if count_open == count_closed == n:
                res.append(''.join(curr))
                return

            if count_open < n:
                curr.append('(')
                dfs(count_open + 1, count_closed, curr)
                curr.pop()
            if count_closed < count_open and count_closed < n:
                curr.append(')')
                dfs(count_open, count_closed + 1, curr)
                curr.pop()
        
        dfs(0, 0, [])
        return res
            