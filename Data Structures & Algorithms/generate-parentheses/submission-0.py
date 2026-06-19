class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # ["("]
        # .....
        #   ["(", "(", "(", ")", ")", ")"]


        def dfs(cnt_open, cnt_close, curr):
            if cnt_open == n and cnt_close == n:
                res.append(''.join(curr))
                return
            
            
            # decision 1: add a open
            if cnt_open < n:
                curr.append("(")
                dfs(cnt_open + 1, cnt_close, curr)
                curr.pop()

            # decision 2: add close
            if cnt_close < n and cnt_close < cnt_open:
                curr.append(")")
                dfs(cnt_open, cnt_close + 1, curr)
                curr.pop()


        dfs(0, 0, [])
        return res